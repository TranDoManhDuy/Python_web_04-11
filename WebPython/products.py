import rootflaskapp
import datacenter 
# viết các class và function thuộc về product ở đây
# Các class quản lý list chứa Các phương thức xử lý lọc dữ liệu, thêm sửa xóa dữ liệu.
# viết các hàm xử lý và truy vấn, cập nhật dữ liệu SQL tại đây.

# Các route xử lý dữ liệu từ client gửi lên server.
# Các route xử lý dữ liệu từ server trả về client.
class phuongtien():
    def __init__(self) -> None:
        self.__id = ""
        self.__tenphuongtien = ""
        self.__sodangki = ""
        self.__loaiphuongtien = ""
        self.__sochongoi = -1
        self.__tinhtrangxe = ""
        self.__giathue1n = 0
        self.__danhmuc = ""
        
    def setId(self, id: str):
        if len(id) > 0:
            self.__id = id
    def getId(self):
        return self.__id
    def setTenhuongtien(self, tenphuongtien: str):
        if len(tenphuongtien) > 0:
            self.__tenphuongtien = tenphuongtien
    def getTenphuongtien(self):
        return self.__tenphuongtien
    
    def setSodangki(self, sodangki: str):
        if len(sodangki) == 9:
            self.__sodangki = sodangki
    def getSodangki(self):
        return self.__sodangki
    
    def setLoaiphuongtien(self, loaiphuongtien: str):
        if loaiphuongtien in ['Sedan', 'SUV', 'Crossover', 'Convertible', 'Hatchback', 'Wagon', 'Van', 'Minivan', 'Coupe']:
            self.__loaiphuongtien = loaiphuongtien
    def getLoaiphuongtien(self):
        return self.__loaiphuongtien
    
    def setSochongoi(self, sochongoi: int):
        if sochongoi > 0:
            self.__sochongoi = sochongoi
    def getSochongoi(self):
        return self.__sochongoi
    
    def setTinhtrangxe(self, tinhtrangxe: int):
        if tinhtrangxe >= 0 and tinhtrangxe <= 100:
            self.__tinhtrangxe = tinhtrangxe
    def getTinhtrangxe(self):
        return self.__tinhtrangxe
    
    def setGiathue1n(self, giathue1n: float):
        if giathue1n > 0:
            self.__giathue1n = giathue1n
    def getGiathua1n(self):
        return self.__giathue1n    
    
    def setDanhmuc(self, danhmuc: str):
        if danhmuc != "":
            self.__danhmuc = danhmuc
    def getDanhmuc(self):
        return self.__danhmuc
    
    def __str__(self) -> str:
        return self.__tenphuongtien + " " + self.__sodangki + " " + self.__loaiphuongtien + " " + str(self.__sochongoi) + " " + self.__tinhtrangxe + " " + str(self.__giathue1n) + " " + self.__danhmuc
    
    # trả về dictionary
    def to_dict(self):
        return {
            "id": self.__id,
            "danhmuc": self.__danhmuc,
            "loaiphuongtien": self.__loaiphuongtien,
            "sodangki": self.__sodangki,
            "tenphuongtien": self.__tenphuongtien,
            "sochongoi": self.__sochongoi,
            "giathue1n": self.__giathue1n,
            "tinhtrangxe": self.__tinhtrangxe
        }
class danhsachphuongtien():
    def __init__(self) -> None:
        self.__danhsachphuongtien = []
    def themphuongtien(self, phuongtien: phuongtien):
        if phuongtien.getSodangki() in [pt.getSodangki() for pt in self.__danhsachphuongtien]:
            return
        self.__danhsachphuongtien.append(phuongtien)
    def layPttheoSDK(self, sodangki):
        for pt in self.__danhsachphuongtien:
            if pt.getSodangki() == sodangki:
                return pt
        return None
    def layDSPttheoTen(self, tenphuongtien):
        dspt = []
        for pt in self.__danhsachphuongtien:
            if tenphuongtien in pt.getTenphuongtien():
                dspt.append(pt.to_dict())
        return dspt
    def getlist(self):
        return [pt.to_dict() for pt in self.__danhsachphuongtien]
    def clearList(self):
        self.__danhsachphuongtien.clear()
    
danhsachPT = danhsachphuongtien()
def fetchDataFromDB():
    command = "SELECT * FROM VEHICLE"
    data = datacenter.takedata(command)
    danhsachPT.clearList()
    for i in data:
        pt = phuongtien()
        pt.setId(str(i[0]).rjust(5, "0"))
        pt.setDanhmuc(i[1])
        pt.setLoaiphuongtien(i[2])
        pt.setSodangki(i[3])
        pt.setTenhuongtien(i[4])
        pt.setSochongoi(i[5])
        pt.setGiathue1n(i[6])
        pt.setTinhtrangxe(i[7])
        danhsachPT.themphuongtien(pt)
        
@rootflaskapp.app.route("/products_getListPT", methods=["GET"])
def products_getListPT():
    if rootflaskapp.request.method == "GET":
        fetchDataFromDB()
        return rootflaskapp.jsonify(danhsachPT.getlist())
    
@rootflaskapp.app.route("/products_addPT", methods=["POST"])
def products_addPT():
    if rootflaskapp.request.method == "POST":
        data = rootflaskapp.request.get_json()
        pt = phuongtien()
        pt.setTenhuongtien(data["tenphuongtien"])
        pt.setSodangki(data["sodangki"])
        pt.setLoaiphuongtien(data["loaiphuongtien"])
        pt.setSochongoi(data["sochongoi"])
        pt.setTinhtrangxe(data["tinhtrangxe"])
        pt.setGiathue1n(data["giathue1n"])
        pt.setDanhmuc(data["danhmuc"])
        danhsachPT.themphuongtien(pt)
        return rootflaskapp.jsonify({"status": "success"})

@rootflaskapp.app.route("/products_getPT", methods=["POST"])
def products_getPT():
    if rootflaskapp.request.method == "POST":
        data = rootflaskapp.request.get_json()
        pt = danhsachPT.layPttheoSDK(data["sodangki"])
        if pt == None:
            return rootflaskapp.jsonify({"status": "fail"})
        return rootflaskapp.jsonify(pt.to_dict())

@rootflaskapp.app.route("/products_getListPTtheoTen", methods=["POST"])
def products_getListPTtheoTen():
    if rootflaskapp.request.method == "POST":
        print(rootflaskapp.request.get_json()["tenphuongtien"])
        data = rootflaskapp.request.get_json()
        dspt = danhsachPT.layDSPttheoTen(data["tenphuongtien"])
        return rootflaskapp.jsonify(dspt)
    
@rootflaskapp.app.route("/products_updatePT", methods=["POST"])
def products_updatePT():
    if rootflaskapp.request.method == "POST":
        data = rootflaskapp.request.get_json()
        pt = danhsachPT.layPttheoSDK(data["sodangki"])
        if pt == None:
            return rootflaskapp.jsonify({"status": "fail"})
        pt.setTenhuongtien(data["tenphuongtien"])
        pt.setLoaiphuongtien(data["loaiphuongtien"])
        pt.setSochongoi(data["sochongoi"])
        pt.setTinhtrangxe(data["tinhtrangxe"])
        pt.setGiathue1n(data["giathue1n"])
        pt.setDanhmuc(data["danhmuc"])
        return rootflaskapp.jsonify({"status": "success"})

# cac ham run khi tai trang      
def run_product():
    fetchDataFromDB()
run_product()

# chuyen qua trang them phuong tien
@rootflaskapp.app.route("/chuyentrang_addProduct")
def chuyentrang_addProduct():
    return rootflaskapp.redirect(rootflaskapp.url_for("products_add"))


@rootflaskapp.app.route("/products_list")
def products_list():
    return rootflaskapp.render_template("views/products/list-product.html")

@rootflaskapp.app.route("/products_add")
def products_add():
    return rootflaskapp.render_template("views/products/add-product.html")

@rootflaskapp.app.route("/products_edit")
def products_edit():
    return rootflaskapp.render_template("views/products/edit-product.html")