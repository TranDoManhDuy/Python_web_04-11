import rootflaskapp
import sqlite3
from datetime import datetime
from flask import request, redirect, url_for

# Utility functions

def validate_date(date_text):
    """Validates date format as YYYY-MM-DD."""
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def takedata(query):
    """Fetches data from the database."""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data

def pushdata(query, params=None):
    """Executes insert/update queries on the database."""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(query, params or ())
    conn.commit()
    conn.close()

class Rental:
    def __init__(self, Id, IDStaff, IDCustomer, IDVehicle, DateRentStart, DateRentEnd, Status):
        self.__Id = Id
        self.__IDStaff = IDStaff
        self.__IDCustomer = IDCustomer
        self.__IDVehicle = IDVehicle
        if validate_date(DateRentStart):
            self.__DateRentStart = DateRentStart
        else:
            raise ValueError("Invalid start date format")
        if validate_date(DateRentEnd):
            self.__DateRentEnd = DateRentEnd
        else:
            raise ValueError("Invalid end date format")
        if Status in [0, 1]:
            self.__Status = Status
        else:
            raise ValueError("Status must be 0 or 1")

    def to_dict(self):
        return {
            'Id': self.__Id,
            'IDStaff': self.__IDStaff,
            'IDCustomer': self.__IDCustomer,
            'IDVehicle': self.__IDVehicle,
            'DateRentStart': self.__DateRentStart,
            'DateRentEnd': self.__DateRentEnd,
            'Status': self.__Status
        }

class Rentals:
    def __init__(self):
        self.__rentals = []
        data = takedata("SELECT * FROM users")
        for i in data:
            rental = Rental(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
            self.__rentals.append(rental)

    def getRentals(self):
        return [r.to_dict() for r in self.__rentals]

    def getRentalById(self, Id):
        data = takedata("SELECT * FROM users WHERE ID = ?", (Id,))
        if data:
            return Rental(*data[0])
        return None

    def addRental(self, rental):
        pushdata("INSERT INTO users (ID, IDStaff, IDCustomer, IDVehicle, DateRentStart, DateRentEnd, Status) "
                 "VALUES (?, ?, ?, ?, ?, ?, ?)", 
                 (rental.getId(), rental.getIDStaff(), rental.getIDCustomer(), rental.getIDVehicle(), 
                  rental.getDateRentStart(), rental.getDateRentEnd(), rental.getStatus()))

    def updateRental(self, Id, rental):
        pushdata("UPDATE users SET IDStaff = ?, IDCustomer = ?, IDVehicle = ?, DateRentStart = ?, "
                 "DateRentEnd = ?, Status = ? WHERE ID = ?",
                 (rental.getIDStaff(), rental.getIDCustomer(), rental.getIDVehicle(), 
                  rental.getDateRentStart(), rental.getDateRentEnd(), rental.getStatus(), Id))

@rootflaskapp.app.route("/list_users")
def list_user():
    rentals = Rentals().getRentals()
    return rootflaskapp.render_template("views/users/list-user.html", rentals=rentals)

@rootflaskapp.app.route("/edit_user/<string:Id>", methods=["GET", "POST"])
def edit_user(Id):
    rentals = Rentals()
    rental = rentals.getRentalById(Id)
    if request.method == "POST":
        IDStaff = request.form["IDStaff"]
        IDCustomer = request.form["IDCustomer"]
        IDVehicle = request.form["IDVehicle"]
        DateRentStart = request.form["DateRentStart"]
        DateRentEnd = request.form["DateRentEnd"]
        Status = int(request.form["Status"])
        updated_rental = Rental(Id, IDStaff, IDCustomer, IDVehicle, DateRentStart, DateRentEnd, Status)
        rentals.updateRental(Id, updated_rental)
        return redirect(url_for("list_user"))
    return rootflaskapp.render_template("views/users/edit-user.html", rental=rental.to_dict() if rental else None)

@rootflaskapp.app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        ID = request.form["ID"]
        IDStaff = request.form["IDStaff"]
        IDCustomer = request.form["IDCustomer"]
        IDVehicle = request.form["IDVehicle"]
        DateRentStart = request.form["DateRentStart"]
        DateRentEnd = request.form["DateRentEnd"]
        Status = int(request.form["Status"])
        new_rental = Rental(ID, IDStaff, IDCustomer, IDVehicle, DateRentStart, DateRentEnd, Status)
        Rentals().addRental(new_rental)
        return redirect(url_for("list_user"))
    return rootflaskapp.render_template("views/users/add-user.html")
