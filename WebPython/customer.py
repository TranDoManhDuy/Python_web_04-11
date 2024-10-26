import rootflaskapp
import sqlite3
import re
# them, sua, khởi tạo lấy duư liệu từ sql (xong)
# regex (xong)
# ho tro tim kiem
# lấy dữ liệu từ sql (tạm ổn)

/////////////////////////////////////

# /////////////////////khach hang////////////////////////////////////


class Name:
    def __init__(self, Lname, Fname):
        self.Fname = Fname
        self.Lname = Lname

    def __str__(self):
        if self == None:
            return "This name is None"
        else:
            return f"Name: {self.Lname} {self.Fname}"


class Customer:  # khach hang so it
    def __init__(self, SSN, Lname, Fname, IDlicense, email,  Phone):
        self.__Id = None   # sẽ sinh tự động "000000000 - 999999999"
        self.__SSN = str(SSN)  # unique
        self.__name = Name(Lname, Fname)
        self.__Idlicense = IDlicense  # unique
        if email == None:
            self.__email = None
        elif validate_email(email) == True:
            self.__email = email
        else:
            self.__email = "Email is not valid"
        self.__phone = Phone

    def __str__(self):
        return f"Id: {self.__Id}, SSN: {self.__SSN}, Name: {self.__name}, Idlicense: {self.__Idlicense}, Email: {self.__email}, Phone: {self.__phone}"

    def setCustomer(self, customer):
        # customer = Customer(customer)
        self.__SSN = customer.getSSN() if customer.getSSN() != None else self.__SSN
        self.__name.Fname = customer.getName().Fname if customer.getName(
        ).Fname != None else self.__name.Fname
        self.__name.Lname = customer.getName().Lname if customer.getName(
        ).Lname != None else self.__name.Lname
        self.__Idlicense = customer.getIdlicense(
        ) if customer.getIdlicense() != None else self.__Idlicense
        self.__email = customer.getEmail() if customer.getEmail() != None else self.__email
        self.__phone = customer.getPhone() if customer.getPhone() != None else self.__phone

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

    def addClient(self, customer):  # thêm khách hàng
        if not isinstance(customer, Customer):
            print("customer is not instance of Customer")
        elif [] != list(filter(lambda x: x.getSSN() == customer.getSSN(), self.__customers)):
            print("SSN is exist")
        elif [] != list(filter(lambda x: x.getIdlicense() == customer.getIdlicense(), self.__customers)):
            print("Idlicense is exist")
        elif customer.getEmail() == "Email is not valid":
            print("Email is not valid")
        else:
            Customers.oldestId += 1
            customer.setId(str(Customers.oldestId).zfill(9))
            self.__customers.append(customer)
            return True
        return False

    def getClients(self):
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

    def getClientOfIndex(self, index):  # lấy thông tin khách hàng theo index
        return self.__customers[index]

    def updateClient(self, Id, customer):  # sửa thông tin khách hàng
        if not isinstance(customer, Customer):
            print("customer is not instance of Customers")
        elif [] != list(filter(lambda x: x.getIdlicense() == customer.getIdlicense(), self.__customers)):
            print("Idlicense is exist")
        elif [] != list(filter(lambda x: x.getSSN() == customer.getSSN(), self.__customers)):
            print("SSN is exist")
        else:
            self.__customers[self.__customers.index(
                self.getClientOfId(Id))].setCustomer(customer)
            return True
        return False

    def removeIndex(self, index):  # chac la khong sài dau
        self.__customers.pop(index)

    def removeId(self, Id):  # chac la khong sài dau
        a = list(filter(lambda x: x.Id == Id, self.__customers))
        self.__customers.remove(a[0])

    def __str__(self):
        return f"{self.__customers}"
# /////////////////////regex, hỗ trợ tìm kiếm///////////////////////


def validate_email(email):
    return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))


def checkOpen(st, code):
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


# /////////////////////test////////////////////////////////////
if __name__ == "__main__":
    print('test')
    customers = Customers()
    customers.addClient(Customer("000000001", "Nguyen", "Van A",
                        "123456789", "123456789@gmail.com", "123456789"))
    customers.addClient(Customer("000000002", "Tran", "Van B",
                        "123456780", "123456789@gmail.com", "123456789"))

    customers.addClient(Customer("000000003", "Trinh", "Van C",
                        "123455781", "123456789@gmail.com", "123456789"))
    customers.addClient(Customer("000000005", "Vo", "Van D",
                        "123455782", "123456789@gmail.com", "123456789"))
    print('\n'.join(map(str, customers.getClients())))
    print('-----------------------------')
    a = customers.getClientOfSSN('000000005').getId()
    customers.updateClient(a, Customer(
        "000000007", None, None, "123456782", None, None))
    print('\n'.join(map(str, customers.getClients())))
    # ////////////////////////////////////////////////////////////

@rootflaskapp.app.route('/customer_list')
def customer_list():
    return rootflaskapp.render_template('views/customer/list-customer.html')

@rootflaskapp.app.route('/customer_edit')
def customer_edit():
    return rootflaskapp.render_template('views/customer/edit-customer.html')

@rootflaskapp.app.route('/customer_add')
def customer_add():
    return rootflaskapp.render_template('views/customer/add-customer.html')