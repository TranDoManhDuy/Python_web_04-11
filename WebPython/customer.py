import rootflaskapp
import sqlite3
import re
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
        return f"Name: {self.Lname} {self.Fname}"


class Client:  # khach hang so it
    def __init__(self, Id, Lname, Fname, email,  phone, IDlicense):
        self.__Id = Id
        self.__name = Name(Lname, Fname)
        if validate_email(email) == True:
            self.__email = email
        else:
            self.__email = "Email is not valid"
        self.__phone = phone
        self.__Idlicense = IDlicense
    def __str__(self):
        return f"Id: {self.__Id}, Name: {self.__name}, Email: {self.__email}, Phone: {self.__phone}, Idlicense: {self.__Idlicense}"

    def getId(self):
        return self.__Id

    def getName(self):
        return self.__name

    def getEmail(self):
        return self.__email

    def getPhone(self):
        return self.__phone

    def getIdlicense(self):
        return self.__Idlicense


class Clients:  # khach hang so nhieu
    def __init__(self):
        self.__clients = []
        data = takedata("SELECT * FROM khachhang")
        for i in data:
            client = Client(i[0], i[1], i[2], i[3], i[4], i[5])
            self.__clients.append(client)

    def addClient(self, client):  # thêm khách hàng
        if not isinstance(client, Client):
            print("client is not instance of Client")
        elif [] != list(filter(lambda x: x.getId() == client.getId(), self.__clients)):
            print("Id is exist")
        elif [] != list(filter(lambda x: x.getIdlicense() == client.getIdlicense(), self.__clients)):
            print("Idlicense is exist")
        elif client.getEmail() == "Email is not valid":
            print("Email is not valid")
        else:
            self.__clients.append(client)
            pushdata(f"INSERT INTO khachhang VALUES ({client.getId()}, '{client.getName().Lname}', '{
                     client.getName().Fname}', '{client.getEmail()}', '{client.getPhone()}', '{client.getIdlicense()}')")
            return True
        return False

    def getClients(self):
        return self.__clients

    def getClientOfId(self, Id):  # lấy thông tin khách hàng theo Id
        a = list(filter(lambda x: x.getId() == Id, self.__clients))
        if a == []:
            return None
        return a[0]

    def getClientOfIndex(self, index):  # lấy thông tin khách hàng theo index
        return self.__clients[index]

    def updateClient(self, Id, client):  # sửa thông tin khách hàng
        if not isinstance(client, Client):
            print("client is not instance of Client")
        elif self.getClientOfId(Id) == None:
            print("Id is not exist")
        elif self.getClientOfId(Id).getId() != client.getId():
            print("client is exist")
        else:
            self.__clients[self.__clients.index(
                self.getClientOfId(Id))] = client
            pushdata(f"UPDATE khachhang SET soCCCD = {client.getId()}, ho = '{client.getName().Lname}', ten = '{client.getName().Fname}', email = '{
                     client.getEmail()}', sdt = '{client.getPhone()}', idBanglaixe = '{client.getIdlicense()}' WHERE soCCCD = {Id}")
            return True
        return False

    def removeIndex(self, index):  # chac la khong sài dau
        self.__clients.pop(index)

    def removeId(self, Id):  # chac la khong sài dau
        a = list(filter(lambda x: x.Id == Id, self.__clients))
        self.__clients.remove(a[0])

    def __str__(self):
        return f"{self.__clients}"
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

    # clients = Clients()
    # m = clients.getClientOfId('898603590447')
    # n = Client('898603590447', m.getName().Lname, "Anh",
    #            m.getEmail(), "1112111111", m.getIdlicense())
    # clients.updateClient(str(898603590447), n)
    # print("\n".join(map(str, clients.getClients())))

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