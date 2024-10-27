import rootflaskapp
import re
import datacenter
# them, sua, khởi tạo lấy duư liệu từ sql (xong)
# regex (xong)
# ho tro tim kiem
# lấy dữ liệu từ sql (tạm ổn)
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

    def setCustomer(self, customer):
        # customer = Customer(customer)
        self.__SSN = customer.getSSN() if customer.getSSN() != None and len(
            customer.getSSN()) == 12 else self.__SSN
        self.__name.Fname = customer.getName().Fname if customer.getName(
        ).Fname != None else self.__name.Fname
        self.__name.Lname = customer.getName().Lname if customer.getName(
        ).Lname != None else self.__name.Lname
        self.__Idlicense = customer.getIdlicense(
        ) if customer.getIdlicense() != None and len(customer.getIdlicense) == 12 else self.__Idlicense
        self.__email = customer.getEmail() if customer.getEmail() != None else self.__email
        self.__phone = customer.getPhone() if customer.getPhone(
        ) != None and len(customer.getPhone()) == 10 else self.__phone

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
            self.oldestId = int(data[1][0])

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
            Customers.oldestId += 1
            customer.setId(str(Customers.oldestId).zfill(9))
            self.__customers.append(customer)
            datacenter.pushdata(f"INSERT INTO CUSTOMER VALUES ('{customer.getId()}', '{customer.getSSN()}', '{
                                customer.getName().Lname}', '{customer.getName().Fname}', '{customer.getIdlicense()}', '{customer.getEmail()}', '{customer.getPhone()}')")
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
            customer_need_update = self.getCustomersOfId(Id)
            customer_need_update.setCustomer(customer)
            # print(f"UPDATE CUSTOMER SET SSN = {customer_need_update.getSSN()}, LastName = {customer_need_update.getName().Lname}, FistName = {customer_need_update.getName(
            # ).Fname}, License = {customer_need_update.getIdlicense()}, Email = {customer_need_update.getEmail()}, PhoneNumber = {customer_need_update.getPhone()} WHERE Id = {Id}")
            datacenter.pushdata(f"UPDATE CUSTOMER SET SSN = '{customer_need_update.getSSN()}', LastName = '{customer_need_update.getName().Lname}', FirstName = '{customer_need_update.getName(
            ).Fname}', License = '{customer_need_update.getIdlicense()}', Email = '{customer_need_update.getEmail()}', PhoneNumber = '{customer_need_update.getPhone()}' WHERE Id = '{Id}'")
            return True
        return False

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
# if __name__ == "__main__":
#     print('test')
#     customers = Customers()
#     print('\n'.join(map(str, customers.getClients())))
#     print('-----------------------------')
#     a = customers.getClientOfSSN('012345678915').getId()
#     customers.updateClient(a, Customer(
#         "012345678910", None, None, None, None, None))
#     print('\n'.join(map(str, customers.getClients())))
    # ////////////////////////////////////////////////////////////
# khởi tạo dữ liệu Customers
flaskCustomers = Customers()


@rootflaskapp.app.route('/customer_list')
def customer_list():
    return rootflaskapp.render_template('views/customer/list-customer.html')


@rootflaskapp.app.route('/customer_edit')
def customer_edit():
    return rootflaskapp.render_template('views/customer/edit-customer.html')


@rootflaskapp.app.route('/customer_add')
def customer_add():
    return rootflaskapp.render_template('views/customer/add-customer.html')
