import rootflaskapp

# viết các class và function thuộc về product ở đây
# Các class quản lý list chứa Các phương thức xử lý lọc dữ liệu, thêm sửa xóa dữ liệu.
# Các hàm xử lý các ngoại lệ, các ràng buộc về dữ liệu. so sánh khớp mẫu. (Ví dụ: regex email, password)
# viết các hàm xử lý và truy vấn, cập nhật dữ liệu SQL tại đây.

# Các route xử lý dữ liệu từ client gửi lên server.
# Các route xử lý dữ liệu từ server trả về client.
class phuongtien():
    def __init__(self) -> None:
        self.__tenphuongtien = ""
        self.__sodangki = ""
        self.__loaiphuongtien = ""
        self.__sochongoi = -1
        self.__tinhtrangxe = ""
        self.__giathue1n = 0
        self.__danhmuc = ""
    def setTenhuongtien(self, tenphuongtien):
        if len(tenphuongtien) > 0:
            self.__tenphuongtien = tenphuongtien
    def getTenphuongtien(self):
        return self.__tenphuongtien
    
    def setSodangki(self, sodangki):
        if len(sodangki) == 9:
            self.__sodangki = sodangki
    def getSodangki(self):
        return self.__sodangki
    
    def setLoaiphuongtien(self, loaiphuongtien):
        if loaiphuongtien in ['Sedan', 'SUV', 'Crossover', 'Convertible', 'Hatchback', 'Wagon', 'Van', 'Minivan', 'Coupe']:
            self.__loaiphuongtien = loaiphuongtien
    def getLoaiphuongtien(self):
        return self.__loaiphuongtien
    
    def setSochongoi(self, sochongoi):
        if sochongoi > 0:
            self.__sochongoi = sochongoi
    def getSochongoi(self):
        return self.__sochongoi
    
    def setTinhtrangxe(self, tinhtrangxe):
        if tinhtrangxe in ['san sang', 'het hang']:
            self.__tinhtrangxe = tinhtrangxe
    def getTinhtrangxe(self):
        return self.__tinhtrangxe
    
    def setGiathue1n(self, giathue1n):
        if giathue1n > 0:
            self.__giathue1n = giathue1n
    def getGiathua1n(self):
        return self.__giathue1n    
    
    def setDanhmuc(self, danhmuc):
        if danhmuc != "":
            self.__danhmuc = danhmuc
    def getDanhmuc(self):
        return self.__danhmuc
    
    def __str__(self) -> str:
        return self.__tenphuongtien + " " + self.__sodangki + " " + self.__loaiphuongtien + " " + str(self.__sochongoi) + " " + self.__tinhtrangxe + " " + str(self.__giathue1n) + " " + self.__danhmuc
    
    # trả về dictionary
    def to_dict(self):
        return {
            "tenphuongtien": self.__tenphuongtien,
            "sodangki": self.__sodangki,
            "loaiphuongtien": self.__loaiphuongtien,
            "sochongoi": self.__sochongoi,
            "tinhtrangxe": self.__tinhtrangxe,
            "giathue1n": self.__giathue1n,
            "danhmuc": self.__danhmuc
        }
@rootflaskapp.app.route("/products_list")
def products_list():
    return rootflaskapp.render_template("views/products/list-product.html")

@rootflaskapp.app.route("/products_add")
def products_add():
    return rootflaskapp.render_template("views/products/add-product.html")

@rootflaskapp.app.route("/products_edit")
def products_edit():
    return rootflaskapp.render_template("views/products/edit-product.html")