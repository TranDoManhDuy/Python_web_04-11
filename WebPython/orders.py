import rootflaskapp
import rootflaskapp
import datetime
import sqlite3
import enum
# them, sua, khởi tạo lấy duư liệu từ sql
# lấy dữ liệu từ sql
# 
# ///////////////////////////////////////////////////////////


class Time:
    def __init__(self, time):
        try:
            self.date = datetime.datetime.strptime(time, '%Y/%m/%d').date()
        except ValueError as e:
            print(e)
            self.date = None

    def additionTime(self, day):
        return self.date + datetime.timedelta(days=day)

    def setTime(self, year, month, day):
        try:
            self.date = datetime.date(year, month, day)
        except ValueError as e:
            print(e)

    def compareTime(self, time):
        if self.date == None or time.date == None:
            return None
        return self.date > time.date

    def __str__(self):
        if self.date == None:
            return "Ngày không hợp lệ"
        return f"{self.date.year}/{self.date.month}/{self.date.day}"


class Status(enum.Enum):

    chua_thanh_toan = 0
    da_thanh_toan = 1

    def __str__(self):
        return self.value


# /////////////////////hóa đơn////////////////////////////////////


class Order:  # hóa đơn số ít
    def __init__(self, id_Staff, SSN_Customer, id_Products, date_of_booking, date_of_end,  status):
        self.__Id = None  # sẽ sinh tự động "000000000 - 999999999"
        self.__id_Staff = str(id_Staff)  # foreign key
        self.__SSN_Customer = str(SSN_Customer)  # foreign key
        self.__id_Products = str(id_Products)   # foreign key
        # lúc nạp vào là 1 string yyyy/mm/dd
        self.__date_of_booking = Time(date_of_booking)
        self.__date_of_end = Time(date_of_end)  # ngày trả lớn hơn ngày mượn
        if self.__date_of_booking.compareTime(self.__date_of_end) == True:
            self.__date_of_end = None
        self.__unit_price = None
        self.__status = Status(status)

    def setOrder(self, order):
        self.__id_Staff = order.getIdStaff() if order.getIdStaff() != None else self.__id_Staff
        self.__id_Customer = order.getIdCustomer(
        ) if order.getIdCustomer() != None else self.__id_Customer
        self.__id_Products = order.getIdProducts(
        ) if order.getIdProducts() != None else self.__id_Products
        self.__date_of_booking = order.getDateOfBooking(
        ) if order.getDateOfBooking() != None else self.__date_of_booking
        self.__date_of_end = order.getDateOfEnd(
        ) if order.getDateOfEnd() != None else self.__date_of_end
        self.__status = order.getStatus() if order.getStatus() != None else self.__status

    def getId(self):
        return self.__Id

    def setIdOrder(self, id_order):
        self.__id_Order = id_order

    def getIdStaff(self):
        return self.__id_Staff

    def getIdCustomer(self):
        return self.__id_Customer

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
        return f"Id: {self.__id_Order}, IdStaff: {self.__id_Staff}, IdCustomer: {self.__id_Customer}, IdProducts: {self.__id_Products}, DateOfBooking: {self.__date_of_booking}, DateOfEnd: {self.__date_of_end}, Status: {self.__status}"


class Orders:  # hóa đơn số nhiều
    oldest_id = 0

    def __init__(self):
        self.__list_order = []

    def getListOrder(self):
        return self.__list_order

    def getOrderOfId(self, id_order):
        a = list(filter(lambda x: x.getIdOrder() ==
                 id_order, self.__list_order))
        if a == []:
            return None
        return a[0]

    def addOrder(self, order):
        if not isinstance(order, Order):
            print("order is not instance of order")
            # dung lenh sql check id_cutomer, id_products, id_staff ton tai hay ko
        else:
            self.oldest_id += 1
            order.setIdOrder(self.oldest_id)
            self.__list_order.append(order)
            return True
        return False

    def updateOrder(self, id, order):
        if not isinstance(order, Order):
            print("order is not instance of order")
            # dung lenh sql check id_cutomer, id_products, id_staff ton tai hay ko
        else:
            self.getOrderOfId(id).setOrder(order)
            return True
        return False

    def __str__(self):
        return f"{self.__list_order}"


# /////////////////////test////////////////////////////////////
if __name__ == '__main__':
    print("testing")


# ////////////////////////////////////////////////////////////
@rootflaskapp.app.route('/orders_list')
def orders_list():
    return rootflaskapp.render_template('views/orders/list-order.html')


@rootflaskapp.app.route('/orders_add')
def orders_add():
    return rootflaskapp.render_template('views/orders/add-order.html')


@rootflaskapp.app.route('/orders_edit')
def orders_edit():
    return rootflaskapp.render_template('views/orders/edit-order.html')
