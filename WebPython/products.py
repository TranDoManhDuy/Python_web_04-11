import rootflaskapp
# viết các class và function thuộc về product ở đây
# Các class quản lý list chứa Các phương thức xử lý lọc dữ liệu, thêm sửa xóa dữ liệu.
# viết các hàm xử lý và truy vấn, cập nhật dữ liệu SQL tại đây.

# Các route xử lý dữ liệu từ client gửi lên server.
# Các route xử lý dữ liệu từ server trả về client.


@rootflaskapp.app.route("/products_list")
def products_list():
    return rootflaskapp.render_template("views/products/list-product.html")


@rootflaskapp.app.route("/products_add")
def products_add():
    return rootflaskapp.render_template("views/products/add-product.html")


@rootflaskapp.app.route("/products_edit")
def products_edit():
    return rootflaskapp.render_template("views/products/edit-product.html")
