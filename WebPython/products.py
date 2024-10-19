import rootflaskapp

# viết các class và function thuộc về product ở đây
# Các class quản lý list chứa Các phương thức xử lý lọc dữ liệu, thêm sửa xóa dữ liệu.
# Các hàm xử lý các ngoại lệ, các ràng buộc về dữ liệu. so sánh khớp mẫu. (Ví dụ: regex email, password)
# viết các hàm xử lý và truy vấn, cập nhật dữ liệu SQL tại đây.

# Các route xử lý dữ liệu từ client gửi lên server.
# Các route xử lý dữ liệu từ server trả về client.

# them, sua
# regex
# ho tro tim kiem
# ////////////////////////////////////////////////////////////

class Name:
    def __init__(self, Fname, Lname):
        self.Fname = Fname
        self.Lname = Lname

    def __str__(self):
        return f"Name: {self.Fname} {self.Lname}"

# khach hang so it


class Client:
    def __init__(self, Id, Fname, Lname,  phone, IDlicense):
        self.__Id = Id
        self.__name = Name(Fname, Lname)
        self.__phone = phone
        self.__Idlicense = IDlicense

    def __str__(self):
        return f"Id: {self.__Id} Name: {self.__name} Phone: {self.__phone} IDlicense: {self.__Idlicense}"

    def getId(self):
        return self.__Id

    def getIdlicense(self):
        return self.__Idlicense
# khach hang so nhieu


class Clients:
    def __init__(self):
        self.__clients = []

    def add(self, client):
        if not isinstance(client, Client):
            print("client is not instance of Client")
        elif [] != list(filter(lambda x: x.getId() == client.getId(), self.__clients)):
            print("Id is exist")
        elif [] != list(filter(lambda x: x.getIdlicense() == client.getIdlicense(), self.__clients)):
            print("Idlicense is exist")
            return False
        else:
            self.__clients.append(client)
            return True

    def getClients(self):
        return self.__clients

    def getClientOfId(self, Id):
        a = list(filter(lambda x: x.getId() == Id, self.__clients))
        if a == []:
            return None
        return a[0]

    def getClientOfIndex(self, index):
        return self.__clients[index]

    def updateClient(self, Id, client):
        if not isinstance(client, Client):
            print("client is not instance of Client")
        elif self.getClientOfId(Id) == None:
            print("Id is not exist")
        elif self.getClientOfId(Id).getId() != client.getId():
            print("client is exist")
        else:
            self.__clients[self.__clients.index(
                self.getClientOfId(Id))] = client
            return True
        return False

    def removeIndex(self, index):  # chac la khong sài dau
        self.__clients.pop(index)

    def removeId(self, Id):  # chac la khong sài dau
        a = list(filter(lambda x: x.Id == Id, self.__clients))
        self.__clients.remove(a[0])

    def __str__(self):
        return f"{self.__clients}"


# ////////////////////////////////////////////////////////////
# if __name__ == "__main__":
#     # test class Clients
#     clients = Clients()
#     kytu = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#     for i in range(10):
#         clients.add(Client(i+1, "Nguyen", "Van " +
#                     kytu[i], "123456789", str(random.randint(1000000000, 9999999999))))
#     clients.updateClient(5, Client(5, "Tran", "Van k", "123456789", "1111111111"))
#     for i in clients.getClients():
#         print(i)


@rootflaskapp.app.route("/products_list")
def products_list():
    return rootflaskapp.render_template("views/products/list-product.html")


@rootflaskapp.app.route("/products_add")
def products_add():
    return rootflaskapp.render_template("views/products/add-product.html")


@rootflaskapp.app.route("/products_edit")
def products_edit():
    return rootflaskapp.render_template("views/products/edit-product.html")
