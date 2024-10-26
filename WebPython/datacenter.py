import sqlite3
import sqlite3
# c.execute("""
#     CREATE TABLE IF NOT EXISTS CUSTOMER(
#         ID TEXT PRIMARY KEY,
#         SSN TEXT NOT NULL CHECK (LENGTH(SSN) = 12),
#         LastName TEXT NOT NULL CHECK (LENGTH(LastName) > 0),
#         FirstName TEXT NOT NULL CHECK (LENGTH(FirstName) > 0),
#         License TEXT NOT NULL CHECK (LENGTH(License) = 12),
#         Email TEXT NOT NULL CHECK (LENGTH(Email) > 0),
#         PhoneNumber TEXT NOT NULL CHECK (LENGTH(PhoneNumber) = 10)
#     )
# """)
# c.execute("""
#     CREATE TABLE IF NOT EXISTS STAFF (
#         ID TEXT PRIMARY KEY,
#         FullName TEXT NOT NULL CHECK (LENGTH(FullName) > 0),
#         PhoneNumber TEXT NOT NULL CHECK (LENGTH(PhoneNumber) = 10),
#         Address TEXT NOT NULL CHECK (LENGTH(Address) > 0),
#         Salary REAL NOT NULL CHECK (Salary > 0),
#         DateCreate TEXT NOT NULL CHECK (LENGTH(DateCreate) > 0),
#         Position TEXT NOT NULL CHECK (Position IN ('Manager', 'Staff'))
#     )
# """)
# c.execute("""
#     CREATE TABLE IF NOT EXISTS VEHICLE (
#         ID TEXT PRIMARY KEY,
#         Category TEXT NOT NULL CHECK (Category IN ('VinFast', 'Mercedes', 'BMW', 'Toyota', 'Honda', 'Kia', 'Ford', 'Suzuki', 'Hyundai', 'Mazda')),
#         Type TEXT NOT NULL CHECK (Type IN ('Sedan', 'SUV', 'Hatchback', 'Coupe', 'Minivan', 'Cuv', 'Supercar', 'Pickup')),
#         RegistrationPlate TEXT UNIQUE NOT NULL CHECK (LENGTH(RegistrationPlate) > 0),
#         VName TEXT NOT NULL CHECK (LENGTH(VName) > 0),
#         SeatNumber INTEGER NOT NULL CHECK (SeatNumber > 0),
#         Rent REAL NOT NULL CHECK (Rent > 0),
#         Status INTEGER NOT NULL
#     )
# """)
# c.execute("""
#     CREATE TABLE IF NOT EXISTS users (
#         ID TEXT PRIMARY KEY,
#         IDStaff TEXT NOT NULL,
#         IDCustomer TEXT NOT NULL,
#         IDVehicle TEXT NOT NULL,
#         DateRentStart TEXT NOT NULL CHECK (LENGTH(DateRentStart) > 0),
#         DateRentEnd TEXT NOT NULL CHECK (LENGTH(DateRentEnd) > 0),
#         Status INTEGER NOT NULL CHECK (Status IN (0, 1)),
#         FOREIGN KEY (IDStaff) REFERENCES STAFF(ID) ON DELETE CASCADE ON UPDATE CASCADE,
#         FOREIGN KEY (IDCustomer) REFERENCES CUSTOMER(ID) ON DELETE CASCADE ON UPDATE CASCADE,
#         FOREIGN KEY (IDVehicle) REFERENCES VEHICLE(ID) ON DELETE CASCADE ON UPDATE CASCADE
#     )
# """)
## MM/DD/YYYY
def takedata(lenh):  # lenh truy van sql
    with sqlite3.connect('WebPython/data.db') as conn:
        c = conn.cursor()
        c.execute(lenh)
        respon = c.fetchall()
        return respon
    
def pushdata(lenh):  # lenh truy van sql
    with sqlite3.connect('WebPython/data.db') as conn:
        c = conn.cursor()
        c.execute(lenh)
        conn.commit()
        return True