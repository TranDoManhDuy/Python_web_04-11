import rootflaskapp
import re
import datacenter
# /////////////////////khach hang////////////////////////////////////


class Name:
    def __init__(self, Lname, Fname):
        self.Fname = Fname
        self.Lname = Lname

    def __str__(self):
        if self == None:
            return "This name is None"
        else:
            return f"{self.Lname} {self.Fname}"


class Customer:  # khach hang so it
    def __init__(self, SSN, Lname, Fname, IDlicense, email,  Phone):
        self.__Id = None   # sẽ sinh tự động "000000000 - 999999999"
        self.__SSN = str(SSN) if len(
            str(SSN)) == 12 else None    # unique 12 so
        self.__name = Name(Lname, Fname)
        self.__Idlicense = str(IDlicense) if len(
            str(IDlicense)) == 12 else None  # unique 12 so
        if email == None:
            self.__email = None
        elif validate_email(email) == True:
            self.__email = email
        else:
            self.__email = "Email is not valid"
        self.__phone = str(Phone) if len(
            str(Phone)) == 10 else None  # unique 10 so

    def __str__(self):
        return f"Id: {self.__Id}, SSN: {self.__SSN}, Name: {self.__name}, Idlicense: {self.__Idlicense}, Email: {self.__email}, Phone: {self.__phone}"

    def __dir__(self):
        return {"id": self.__Id,
                "SSN": self.__SSN,
                "Fname": self.__name.Fname,
                "Lname": self.__name.Lname,
                "idlicense": self.__Idlicense,
                "email": self.__email,
                "phone": self.__phone}

    def setCustomer(self, customer):
        # customer = Customer(customer)
        self.__SSN = customer.getSSN() if len(
            customer.getSSN()) == 12 else self.__SSN
        self.__name.Fname = customer.getName().Fname
        self.__name.Lname = customer.getName().Lname
        self.__Idlicense = customer.getIdlicense() if len(
            customer.getIdlicense()) == 12 else self.__Idlicense
        self.__email = customer.getEmail() if customer.getEmail() != None else self.__email
        self.__phone = customer.getPhone() if len(
            customer.getPhone()) == 10 else self.__phone

    def getId(self):
        return self.__Id

    def setId(self, Id):
        self.__Id = Id

    def getSSN(self):
        return self.__SSN

    def getName(self):
        return self.__name

    def getIdlicense(self):
        return self.__Idlicense

    def getEmail(self):
        return self.__email

    def getPhone(self):
        return self.__phone


class Customers:  # khach hang so nhieu
    oldestId = 0

    def __init__(self):
        self.__customers = []
        data = datacenter.takedata('SELECT * FROM CUSTOMER')
        if data != []:  # nếu chưa có dữ liệu
            for i in data:
                da = Customer(i[1], i[2], i[3], i[4], i[5], i[6])
                da.setId(i[0])
                self.__customers.append(da)
            self.oldestId = int(data[-1][0])

    def addCutomer(self, customer):  # thêm khách hàng
        if not isinstance(customer, Customer):
            print("customer is not instance of Customer")
        elif [] != list(filter(lambda x: x.getSSN() == customer.getSSN(), self.__customers)) or customer.getSSN() == None:
            print("SSN is exist")
        elif [] != list(filter(lambda x: x.getIdlicense() == customer.getIdlicense(), self.__customers)) or customer.getIdlicense() == None:
            print("Idlicense is exist")
        elif customer.getEmail() == "Email is not valid":
            print("Email is not valid")
        elif customer.getPhone() == None:
            print("Phone is not valid")
        else:
            self.oldestId += 1
            customer.setId(str(self.oldestId).zfill(9))
            self.__customers.append(customer)
            try:
                datacenter.pushdata(f"INSERT INTO CUSTOMER VALUES ('{customer.getId()}', '{customer.getSSN()}', '{
                    customer.getName().Lname}', '{customer.getName().Fname}', '{customer.getIdlicense()}', '{customer.getEmail()}', '{customer.getPhone()}')")
            except:
                print("Error")
            return True
        return False

    def getCustomer(self):
        return self.__customers

    def getCustomersOfId(self, Id):  # lấy thông tin khách hàng theo Id
        a = list(filter(lambda x: x.getId() == Id, self.__customers))
        if a == []:
            return None
        return a[0]

    def getClientOfSSN(self, SSN):  # lấy thông tin khách hàng theo SSN
        a = list(filter(lambda x: x.getSSN() == SSN, self.__customers))
        if a == []:
            return None
        return a[0]

    # lấy thông tin khách hàng theo Idlicense
    def getCustomerOfIdlicense(self, Idlicense):
        a = list(filter(lambda x: x.getIdlicense()
                 == Idlicense, self.__customers))
        if a == []:
            return None
        return a[0]

    def getClientOfIndex(self, index):  # lấy thông tin khách hàng theo index
        return self.__customers[index]

    def getListJson(self):
        return [i.__dir__() for i in self.__customers]

    def getListJsonbyName(self, name):

        return [i.__dir__() for i in self.__customers if checkOpen(i.getName().__str__(), name)]

    def updateCustomer(self, Id, customer):  # sửa thông tin khách hàng
        if not isinstance(customer, Customer):
            print("customer is not instance of Customers")
        # kiểm tra xem có trùng Idlicense không
        elif [] != list(filter(lambda x: x.getIdlicense() == customer.getIdlicense(), self.__customers)) and self.getCustomersOfId(Id).getIdlicense() != customer.getIdlicense():
            print("Idlicense is exist")
        # kiểm tra xem có trùng SSN không
        elif [] != list(filter(lambda x: x.getSSN() == customer.getSSN(), self.__customers)) and self.getCustomersOfId(Id).getSSN() != customer.getSSN():
            print("SSN is exist")
        else:
            customer_need_update = self.getCustomersOfId(Id)
            customer_need_update.setCustomer(customer)
            ssn = customer_need_update.getSSN()
            lastname = customer_need_update.getName().Lname
            firstname = customer_need_update.getName().Fname
            idlicense = customer_need_update.getIdlicense()
            email = customer_need_update.getEmail()
            phone = customer_need_update.getPhone()
            datacenter.pushdata(f"UPDATE CUSTOMER SET SSN = '{ssn}', LastName = '{lastname}', FirstName = '{
                                firstname}', License = '{idlicense}', Email = '{email}', PhoneNumber = '{phone}' WHERE ID = '{Id}'")
            print("testing")
            return True
        return False

    def __str__(self):
        return f"{self.__customers}"
# /////////////////////regex, hỗ trợ tìm kiếm///////////////////////


def validate_email(email):
    return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))


def checkOpen(stin, codein):
    if codein == "":
        return True

    st = stin.lower()
    code = codein.lower()
    for i in range(len(st)):
        if st[i] == code[0]:
            j1, j2 = i, 0
            while j1 < len(st):
                if st[j1] == code[j2]:
                    j2 += 1
                j1 += 1
                if j2 == len(code):
                    return True
    return False


def searchOpen(ds, code):
    resulf = []
    for i in range(len(ds)):
        if checkOpen(ds[i], code):
            resulf.append(ds[i])
    return resulf


def checkName(name):
    pattern = r'^[a-zA-Z\s]+$'
    if re.match(pattern, name):
        return name.title()
    return False


# khởi tạo dữ liệu Customers
flaskCustomers = Customers()

# //////////////////////////////////////////////////////////////////////////////


@rootflaskapp.app.route('/chuyentrang_fixCustomer', methods=["GET"])
def chuyentrang_fixCustomer():
    return rootflaskapp.redirect(rootflaskapp.url_for("customer_edit"))


@rootflaskapp.app.route('/getIDCustomerForFix', methods=["POST"])
def getIDCustomerForFix():
    if rootflaskapp.request.method == 'POST':
        data = rootflaskapp.request.get_json()
        print(data, "DATA_____________________________")
        cu = flaskCustomers.getCustomersOfId(data["id"]).__dir__()
        global fixCustomer
        fixCustomer = cu
        return rootflaskapp.jsonify({"status": "success", "Custonmer": cu})


@rootflaskapp.app.route('/chuyentrang_addCustomer')
def chuyentrang_addCustomer():
    return rootflaskapp.redirect(rootflaskapp.url_for("customer_add"))


@rootflaskapp.app.route('/getListKHtheoTen', methods=["POST"])
def getlistCustomertheoTen():
    if rootflaskapp.request.method == 'POST':
        data = rootflaskapp.request.get_json()
        return flaskCustomers.getListJsonbyName(data["Fullname"])


@rootflaskapp.app.route('/Customers_getListKH', methods=["GET"])
def getlistCustomer():
    if rootflaskapp.request.method == 'GET':
        return rootflaskapp.jsonify(flaskCustomers.getListJson())


@rootflaskapp.app.route('/customer_list')
def customer_list():
    return rootflaskapp.render_template('views/customer/list-customer.html')

# customer_add


@rootflaskapp.app.route('/themCustomer', methods=["POST"])
def addCustomers():
    if rootflaskapp.request.method == 'POST':
        data = rootflaskapp.request.get_json()
        customer = Customer(data["cccd"], data["lastName"], data["firstName"],
                            data["driverLicenseId"], data["customerEmail"], data["customerPhone"])
        if flaskCustomers.addCutomer(customer) == True:
            return rootflaskapp.jsonify({"status": "success"})
        return rootflaskapp.jsonify({"status": "fail"})


@rootflaskapp.app.route('/checkDriverLicenseId', methods=["POST"])
def checkDriverLicenseId():
    if rootflaskapp.request.method == 'POST':
        data = rootflaskapp.request.get_json()
        check = flaskCustomers.getCustomerOfIdlicense(data["driverLicenseId"])
        if check == None:
            return rootflaskapp.jsonify({"status": "success"})
        else:
            return rootflaskapp.jsonify({"status": "fail"})


@rootflaskapp.app.route('/checkCCCD', methods=["POST"])
def checkCCCD():
    if rootflaskapp.request.method == 'POST':
        data = rootflaskapp.request.get_json()
        check = flaskCustomers.getClientOfSSN(data["CCCD"])
        if check == None:
            return rootflaskapp.jsonify({"status": "success"})
        else:
            return rootflaskapp.jsonify({"status": "fail"})


@rootflaskapp.app.route('/checkName', methods=["POST"])
def CheckName():
    if rootflaskapp.request.method == 'POST':
        data = rootflaskapp.request.get_json()
        if checkName(data["name"]) == False:
            return rootflaskapp.jsonify({"status": "fail"})
        return rootflaskapp.jsonify({"status": "success",
                                     "name": checkName(data["name"])})


@rootflaskapp.app.route('/checkEmail', methods=["POST"])
def checkEmail():
    if rootflaskapp.request.method == 'POST':
        data = rootflaskapp.request.get_json()
        if validate_email(data["email"]) == True:
            return rootflaskapp.jsonify({"status": "success"})
        return rootflaskapp.jsonify({"status": "fail"})


@rootflaskapp.app.route('/chuyentrang_listCustomer', methods=["GET"])
def chuyentrangDSKH():
    print("chuyentrangDSKH------------------------------------")
    return rootflaskapp.redirect(rootflaskapp.url_for("customer_list"))


@rootflaskapp.app.route('/customer_add')
def customer_add():
    return rootflaskapp.render_template('views/customer/add-customer.html')

# customer_edit


@rootflaskapp.app.route('/updateCustomer', methods=["POST"])
def updateCustomer():
    if rootflaskapp.request.method == 'POST':
        data = rootflaskapp.request.get_json()
        customer = Customer(data["CCCD"], data["Lname"], data["Fname"],
                            data["idlicense"], data["email"], data["phone"])

        # execute = """
        #     UPDATE CUSTOMER
        #     SET SSN = '{}', LastName = '{}', FirstName = '{}', License = '{}', Email = '{}', PhoneNumber = '{}'
        #     WHERE ID = '{}'
        # """
        # datacenter.pushdata(execute.format(
        #     customer.getSSN(), customer.getName().Lname, customer.getName().Fname, customer.getIdlicense(), customer.getEmail(), customer.getPhone(), data["id"]))
        if flaskCustomers.updateCustomer(data["id"], customer) == True:
            return rootflaskapp.jsonify({"status": "success"})
        return rootflaskapp.jsonify({"status": "fail"})


@rootflaskapp.app.route('/getCustomerFix')
def getCustomer():
    return rootflaskapp.jsonify(fixCustomer)


@rootflaskapp.app.route('/customer_edit')
def customer_edit():
    return rootflaskapp.render_template('views/customer/edit-customer.html')
