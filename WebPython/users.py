import rootflaskapp
import datacenter
class staff():
    def __init__(self):
        self.ID = ""
        self.FullName = ""
        self.PhoneNumber = ""
        self.Address = ""
        self.Salary = 0.0
        self.Position = ""
    
    def getID(self):
        return str(int(self.ID))
    def setID(self, ID):
        if int(ID) < 0:
            raise ValueError("ID must be a positive integer")
        self.ID = ID
    
    def getFullName(self):
        return self.FullName
    def setFullName(self, FullName):
        if (len(FullName) <= 0):
            raise ValueError("FullName must not be empty")
        self.FullName = FullName
    
    def getPhoneNumber(self):
        return self.PhoneNumber
    def setPhoneNumber(self, PhoneNumber):
        if (len(PhoneNumber) == 10):
            self.PhoneNumber = PhoneNumber
    
    def getAddress(self):
        return self.Address
    def setAddress(self, Address):
        if (len(Address) <= 0):
            raise ValueError("Address must not be empty")
        self.Address = Address
    
    def getSalary(self):
        return self.Salary
    def setSalary(self, Salary):
        if (float(Salary) < 0):
            raise ValueError("Salary must be a positive number")
        self.Salary = Salary
    
    def getPosition(self):
        return self.Position
    def setPosition(self, Position):
        if Position  in ["Manager", "Staff"]:
            self.Position = Position
    def __str__(self):
        return "ID: " + self.ID + ", FullName: " + self.FullName + ", PhoneNumber: " + self.PhoneNumber + ", Address: " + self.Address + ", Salary: " + str(self.Salary) + ", Position: " + self.Position
    
    def to_dict(self):
        return {
            "ID": str(self.ID).rjust(5, '0'),
            "FullName": self.FullName,
            "PhoneNumber": self.PhoneNumber,
            "Address": self.Address,
            "Salary": self.Salary,
            "Position": self.Position
        }

class ListStaff():
    def __init__(self):
        self.listStaff = []
    
    def addStaff(self, staff):
        self.listStaff.append(staff)
    def getLen(self):
        return len(self.listStaff)
    
    def searchStaffByID(self, ID):
        for staff in self.listStaff:
            if staff.getID() == ID:
                return staff
        return None
    
    def searchStaffByFullName(self, FullName):
        result = []
        if FullName["FullName"] == "":
            return self.to_dict()
        for staff in self.listStaff:
            if FullName["FullName"].lower() in staff.getFullName().lower():
                result.append(staff.to_dict())
        return result
    
    def __str__(self):
        result = ""
        for staff in self.listStaff:
            result += staff.__str__() + "\n"
        return result
    
    def to_dict(self):
        result = []
        for staff in self.listStaff:
            result.append(staff.to_dict())
        return result
    def clearList(self):
        self.listStaff = []

listStaff = ListStaff()
staffToEdit = staff()

def fetchDataStaff():
    respon = datacenter.takedata("SELECT * FROM STAFF")
    listStaff.clearList()
    for row in respon:
        s = staff()
        s.setID(row[0])
        s.setFullName(row[1])
        s.setPhoneNumber(row[2])
        s.setAddress(row[3])
        s.setSalary(row[4])
        s.setPosition(row[6])
        listStaff.addStaff(s)

@rootflaskapp.app.route("/getListStaff")
def getListStaff():
    fetchDataStaff()
    return listStaff.to_dict()

@rootflaskapp.app.route("/getListStaffByName", methods=["POST"])
def getListStaffByName():
    FullName = rootflaskapp.request.get_json()
    result = listStaff.searchStaffByFullName(FullName)
    return result

@rootflaskapp.app.route("/postIDStaff", methods=["POST"])  
def postIDStaff():
    ID = rootflaskapp.request.get_json()
    global staffToEdit
    staffToEdit = listStaff.searchStaffByID(str(int(ID)))
    if staffToEdit is not None:
        return staffToEdit.to_dict()
    return {"status": "fail"}

@rootflaskapp.app.route("/updateStaff", methods=["POST"])
def updateStaff():
    staffUpdate = rootflaskapp.request.get_json()
    print(staffUpdate)
    staffToEdit.setFullName(staffUpdate["FullName"])
    staffToEdit.setPhoneNumber(staffUpdate["PhoneNumber"])
    staffToEdit.setAddress(staffUpdate["Address"])
    staffToEdit.setSalary(staffUpdate["Salary"])
    staffToEdit.setPosition(staffUpdate["Position"])
    lenh = """
    UPDATE STAFF SET FullName = '{}', PhoneNumber = '{}', Address = '{}', Salary = {}, Position = '{}' WHERE ID = {}
    """
    datacenter.pushdata(lenh.format(staffToEdit.getFullName(), staffToEdit.getPhoneNumber(), staffToEdit.getAddress(), staffToEdit.getSalary(), staffToEdit.getPosition(), staffToEdit.getID()))
    return {"status": "success"}

@rootflaskapp.app.route("/getEditStaff", methods=["GET"])
def getEditStaff():
    return rootflaskapp.jsonify(staffToEdit.to_dict())


@rootflaskapp.app.route("/addStaff", methods=["POST"])
def addStaff():
    staffAdd = rootflaskapp.request.get_json()
    print(staffAdd)
    s = staff()
    s.setID(listStaff.getLen() + 1)
    s.setFullName(staffAdd["name"])
    s.setPhoneNumber(staffAdd["phone"])
    s.setAddress(staffAdd["address"])
    s.setSalary(staffAdd["salary"])
    s.setPosition(staffAdd["position"])
    lenh = """
    INSERT INTO STAFF VALUES ({}, '{}', '{}', '{}', {}, '{}', '{}')
    """
    datacenter.pushdata(lenh.format(listStaff.getLen() + 1, s.getFullName(), s.getPhoneNumber(), s.getAddress(), s.getSalary(), "*" ,s.getPosition()))
    return rootflaskapp.jsonify({"status": "success"})


def checkExist(ID):
    fetchDataStaff()
    for staff in listStaff.listStaff:
        if staff.getID() == ID:
            return True
    return False

@rootflaskapp.app.route("/list_users")
def list_user():
    return rootflaskapp.render_template("views/users/list-user.html")

@rootflaskapp.app.route("/edit_user")
def edit_user():
    return rootflaskapp.render_template("views/users/edit-user.html")

@rootflaskapp.app.route("/add_user")
def add_user():
    return rootflaskapp.render_template("views/users/add-user.html")

fetchDataStaff()