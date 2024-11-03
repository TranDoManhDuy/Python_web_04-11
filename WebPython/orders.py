import rootflaskapp
import users
import email_automatic
import datetime
import datacenter
import customer as cus  # import customer
import enum
import products as pro  # import product
# them, sua, khởi tạo lấy duư liệu từ sql
# lấy dữ liệu từ sql
#
# ///////////////////////////////////////////////////////////


def transformTime(time: str):
    time = datetime.datetime.strptime(time, '%Y/%m/%d').date()
    return time.strftime('%d/%m/%Y')


def transformTime1(time: str):
    time = datetime.datetime.strptime(time, '%d/%m/%Y').date()
    return time.strftime('%Y/%m/%d')


class Time:
    def __init__(self, time):
        try:
            self.date = datetime.datetime.strptime(time, '%Y/%m/%d').date()
        except ValueError as e:
            print(e)
            self.date = None

    def afitionTime(self, day):
        return (self.date - day.date).days

    def setTime(self, year, month, day):
        try:
            self.date = datetime.date(year, month, day)
        except ValueError as e:
            print(e)

    def compareTime(self, time):
        if self.date == None or time.date == None:
            return None
        return self.date > time.date

    def today(self):
        return datetime.datetime.now().date().strftime('%Y/%m/%d')

    def __str__(self):
        if self.date == None:
            return "Ngày không hợp lệ"
        return f"{self.date.year}/{str(self.date.month).zfill(2)}/{str(self.date.day).zfill(2)}"


class Status(enum.Enum):
    chua_thanh_toan = 0
    da_thanh_toan = 1

    def __str__(self):
        return self.name.replace("_", " ").upper()


# /////////////////////hóa đơn////////////////////////////////////


class Order:  # hóa đơn số ít
    def __init__(self, id_Staff, Id_Customer, id_Products, date_of_booking, date_of_end, status):
        self.__Id = None  # sẽ sinh tự động "000000000 - 999999999"
        self.__id_Staff = str(id_Staff)  # foreign key
        self.__Id_Customer = str(Id_Customer)  # foreign key
        self.__id_Products = str(id_Products)   # foreign key
        # lúc nạp vào là 1 string yyyy/mm/dd
        self.__date_of_booking = Time(date_of_booking)
        self.__date_of_end = Time(date_of_end)  # ngày trả lớn hơn ngày mượn
        self.__unit_price = int(self.__date_of_end.afitionTime(
            self.__date_of_booking)) * pro.danhsachPT.layPttheoID(self.__id_Products).getGiathua1n()
        self.__status = Status(status)  # có thể lỗi

    def setOrder(self, order):
        self.__id_Staff = order.getIdStaff() if order.getIdStaff() != None else self.__id_Staff
        # check xem co ton tai khach hang ko
        self.__Id_Customer = order.getIdCustomer() if cus.flaskCustomers.getCustomersOfId(
            order.getIdCustomer()) != None else self.__Id_Customer
        self.__id_Products = order.getIdProducts() if pro.danhsachPT.layPttheoID(
            order.getIdProducts) != None else self.__id_Products
        self.__date_of_booking = order.getDateOfBooking(
        ) if order.getDateOfBooking() != None else self.__date_of_booking
        self.__date_of_end = order.getDateOfEnd(
        ) if order.getDateOfEnd() != None else self.__date_of_end
        self.__status = order.getStatus() if order.getStatus() != None else self.__status

    def getIdOrder(self):
        return self.__Id

    def setIdOrder(self, id_order):
        self.__Id = id_order

    def getIdStaff(self):
        return self.__id_Staff

    def getIdCustomer(self):
        return self.__Id_Customer

    def getIdProducts(self):
        return self.__id_Products

    def getDateOfBooking(self):
        return self.__date_of_booking

    def getDateOfEnd(self):
        return self.__date_of_end

    def getUnitPrice(self):
        return self.__unit_price

    def getStatus(self):
        return self.__status

    def __str__(self):
        return f"Id: {self.__Id}, IdStaff: {self.__id_Staff}, IdCustomer: {self.__Id_Customer}, IdProducts: {self.__id_Products}, DateOfBooking: {self.__date_of_booking}, DateOfEnd: {self.__date_of_end}, Status: {self.__status}"

    def __dir__(self):
        return {"Id": self.__Id,
                "IdStaff": self.__id_Staff,
                "IdCustomer": cus.flaskCustomers.getCustomersOfId(self.__Id_Customer).getSSN(),
                "IdProducts": pro.danhsachPT.layPttheoID(self.__id_Products).getSodangki(),
                "DateOfBooking": transformTime(self.__date_of_booking.__str__()). replace("/", "-"),
                "DateOfEnd": transformTime(self.__date_of_end.__str__()).replace("/", "-"),
                "UnitPrice": self.__unit_price,
                "Status": self.__status.__str__()}


class Orders:  # hóa đơn số nhiều
    oldest_id = 0

    def __init__(self):
        self.__list_order = []
        data = datacenter.takedata("SELECT * FROM ORDERS")
        for i in data:
            da = Order(i[1], i[2], i[3], i[4], i[5], i[6])
            da.setIdOrder(i[0])
            self.__list_order.append(da)
            self.oldest_id += 1

    def getListOrderByidOpen(self, id):
        return list(filter(lambda x: cus.checkOpen(x.getIdOrder(), id), self.__list_order))

    def getListOrder(self):
        return self.__list_order

    def gitListOrderJson(self):
        return list(map(lambda x: x.__dir__(), self.__list_order))

    def getOrderOfId(self, id_order):
        a = list(filter(lambda x: x.getIdOrder()
                 == id_order, self.__list_order))
        if a == []:
            return None
        return a[0]

    def addOrder(self, order):
        if not isinstance(order, Order):
            print("order is not instance of order")
        elif cus.flaskCustomers.getCustomersOfId(order.getIdCustomer()) == None:
            # check id_customer ton tai hay ko
            print("Customer is not exist")
            # chua check id_products, id_staff ton tai hay ko
        elif pro.danhsachPT.layPttheoID(order.getIdProducts()) == None and order.getIdProducts() != None:
            print("Product is not exist")
        elif order.getDateOfBooking().compareTime(order.getDateOfEnd()) == True:
            print("Date of booking is greater than date of end")
        else:
            self.oldest_id += 1
            order.setIdOrder(str(self.oldest_id).zfill(9))
            self.__list_order.append(order)
            datacenter.pushdata(f"INSERT INTO ORDERS VALUES ('{order.getIdOrder()}', '{order.getIdStaff()}', '{order.getIdCustomer()}', '{
                                int(order.getIdProducts())}', '{order.getDateOfBooking()}', '{order.getDateOfEnd()}', '{order.getStatus().value}')")
            return True
        return False

    def updateOrder(self, id, order):
        if not isinstance(order, Order):
            print("order is not instance of order")
        elif cus.flaskCustomers.getCustomersOfId(order.getIdCustomer()) == None:
            print("Customer is not exist")  # check id_customer ton tai hay ko
        elif pro.danhsachPT.layPttheoID(order.getIdProducts()) == None and order.getIdProducts() != None:
            print("Product is not exist")  # check id_products ton tai hay ko
        elif order.getDateOfBooking().compareTime(order.getDateOfEnd()) == True:
            print("Date of booking is greater than date of end")
        else:
            self.getOrderOfId(id).setOrder(order)
            datacenter.pushdata(f"UPDATE ORDERS SET IDStaff = '{order.getIdStaff()}', IDCustomer = '{order.getIdCustomer()}', IDVehicle = '{int(order.getIdProducts(
            ))}', DateRentStart = '{order.getDateOfBooking()}', DateRentEnd = '{order.getDateOfEnd()}', Status = '{order.getStatus().value}' WHERE ID = '{id}'")

            return True
        return False

    def __str__(self):
        return f"{self.__list_order}"


# /////////////////////test////////////////////////////////////
flaskOrders = Orders()
if __name__ == "__main__":
    pass

# orders_list


@rootflaskapp.app.route('/orders_list')
def orders_list():
    return rootflaskapp.render_template('views/orders/list-order.html')


@rootflaskapp.app.route('/Orders_getListHD', methods=['GET'])
def orders_getListHD():
    return rootflaskapp.jsonify(flaskOrders.gitListOrderJson())


@rootflaskapp.app.route('/Orders_searchHD', methods=['POST'])
def orders_searchHD():
    if rootflaskapp.request.method == 'POST':
        data = rootflaskapp.request.get_json()
        datapush = flaskOrders.getListOrderByidOpen(data['key'])
        datapush = list(map(lambda x: x.__dir__(), datapush))
        return rootflaskapp.jsonify(datapush)


@rootflaskapp.app.route('/getIDOrderForFix', methods=['POST'])
def getIDOrderForFix():
    if rootflaskapp.request.method == 'POST':
        data = rootflaskapp.request.get_json()
        cu = flaskOrders.getOrderOfId(data['id']).__dir__()
        global OrderForFix
        OrderForFix = cu
        return rootflaskapp.jsonify({"status": "success", "order": cu})


@rootflaskapp.app.route('/chuyentrang_fixOrder', methods=['GET'])
def chuyentrang_fixOrder():
    return rootflaskapp.redirect(rootflaskapp.url_for('orders_edit'))

# orders_add


@rootflaskapp.app.route('/addOrder', methods=['POST'])
def addOrder():
    if rootflaskapp.request.method == 'POST':
        data = rootflaskapp.request.get_json()
        if data['Status'] == "Đã thanh toán":
            status = Status.da_thanh_toan
        elif data['Status'] == "Chưa thanh toán":
            status = Status.chua_thanh_toan
        od = Order(data['IdStaff'], cus.flaskCustomers.getClientOfSSN(data['IdCustomer']).getId(
        ), pro.danhsachPT.layPttheoSDK(data['IdProducts'])["id"], str(data['DateOfBooking']).replace('-', '/'), str(data['DateOfEnd']).replace('-', '/'), status.value)
        if flaskOrders.addOrder(od):
            return rootflaskapp.jsonify({"status": "success"})
        if od.getDateOfBooking().compareTime(od.getDateOfEnd()) == True:
            return rootflaskapp.jsonify({"status": "fail1", "error": "Date of booking is greater than date of end"})
        return rootflaskapp.jsonify({"status": "fail"})


@rootflaskapp.app.route('/getNewIdorder')
def getNewIdorder():
    return rootflaskapp.jsonify({"id": str(flaskOrders.oldest_id+1).zfill(9),
                                 "today": Time("2021/1/1").today().replace("/", "-")})


@rootflaskapp.app.route('/orders_add')
def orders_add():
    return rootflaskapp.render_template('views/orders/add-order.html')
# orders_edit


@rootflaskapp.app.route('/editOrder', methods=['POST'])
def editOrder():
    if rootflaskapp.request.method == 'POST':
        data = rootflaskapp.request.get_json()
        if data['Status'] == "Đã thanh toán":
            status = Status.da_thanh_toan
        elif data['Status'] == "Chưa thanh toán":
            status = Status.chua_thanh_toan
        else:
            status = flaskOrders.getOrderOfId(data['Id']).getStatus()
        od = Order(data['IdStaff'], cus.flaskCustomers.getClientOfSSN(data['IdCustomer']).getId(
        ), pro.danhsachPT.layPttheoSDK(data['IdProducts'])["id"], str(data['DateOfBooking']).replace('-', '/'), str(data['DateOfEnd']).replace('-', '/'), status.value)
        if flaskOrders.updateOrder(data['Id'], od):
            return rootflaskapp.jsonify({"status": "success"})
        if od.getDateOfBooking().compareTime(od.getDateOfEnd()) == True:
            return rootflaskapp.jsonify({"status": "fail1", "error": "Date of booking is greater than date of end"})
        return rootflaskapp.jsonify({"status": "fail"})


@rootflaskapp.app.route('/getOrderFix')
def getOrderFix():
    OrderForFix["DateOfBooking"] = transformTime1(
        OrderForFix["DateOfBooking"].replace("-", "/")).replace("/", "-")
    OrderForFix["DateOfEnd"] = transformTime1(
        OrderForFix["DateOfEnd"].replace("-", "/")).replace("/", "-")
    return rootflaskapp.jsonify(OrderForFix)


@rootflaskapp.app.route('/orders_edit')
def orders_edit():
    return rootflaskapp.render_template('views/orders/edit-order.html')

# data = [
#     (2, 102, 1002, 202, "2024-10-03", "2024-10-10", "In Progress"),
#     (3, 103, 1003, 203, "2024-01-05", "2024-10-12", "Cancelled"),
#     (4, 104, 1004, 204, "2024-02-07", "2024-10-14", "Completed"),
#     (5, 105, 1005, 205, "2024-02-09", "2024-10-16", "In Progress"),
#     (6, 106, 1006, 206, "2024-03-11", "2024-10-18", "Completed"),
#     (7, 107, 1007, 207, "2024-04-13", "2024-10-20", "Cancelled"),
#     (8, 108, 1008, 208, "2024-03-15", "2024-10-22", "Completed"),
#     (9, 109, 1009, 209, "2024-03-17", "2024-10-24", "In Progress"),
#     (1, 110, 1010, 210, "2024-03-19", "2024-10-26", "Completed"),
# ]
# result = []
# for i in range(12):
#     result.append(0)
# for i in data:
#     # moi phan tu i la 1 don hang, gia tri moi don hang = PT.giathue * songay
#     month = (datetime.datetime.strptime(i[4], "%Y-%m-%d").month)
#     result[month - 1] += 1 # ket qua cuoi cung moi thang
#     # moi gia tri result la tong doanh thu cua moi thang
# print(result)


@rootflaskapp.app.route('/getStatistical')
def getStatistical():
    pro.fetchDataFromDB()

    lenh = "SELECT * FROM ORDERS"
    data = pro.datacenter.takedata(lenh)
    result = []
    for i in range(12):
        result.append(0)
    for i in data:
        pt = pro.danhsachPT.layPttheoID(i[3]).to_dict()
        month = (datetime.datetime.strptime(i[4], "%Y-%m-%d").month)
        start = datetime.datetime.strptime(i[4], "%Y-%m-%d")
        end = datetime.datetime.strptime(i[5], "%Y-%m-%d")
        result[month - 1] += pt["giathue1n"] * (end - start).days
