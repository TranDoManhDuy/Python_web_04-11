import rootflaskapp
import products
import users
import customer
import email_automatic
import datetime

@rootflaskapp.app.route('/orders_list')
def orders_list():
    return rootflaskapp.render_template('views/orders/list-order.html')

@rootflaskapp.app.route('/orders_add')
def orders_add():
    return rootflaskapp.render_template('views/orders/add-order.html')

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
    products.fetchDataFromDB()
    
    lenh = "SELECT * FROM ORDERS"
    data = products.datacenter.takedata(lenh)
    result = []
    for i in range(12):
        result.append(0)
    for i in data:
        pt = products.danhsachPT.layPttheoID(i[3]).to_dict()
        month = (datetime.datetime.strptime(i[4], "%Y-%m-%d").month)
        start = datetime.datetime.strptime(i[4], "%Y-%m-%d")
        end = datetime.datetime.strptime(i[5], "%Y-%m-%d")
        result[month - 1] += pt["giathue1n"] * (end - start).days