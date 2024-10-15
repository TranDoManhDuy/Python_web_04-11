import rootflaskapp

@rootflaskapp.app.route("/products_list")
def products_list():
    return rootflaskapp.render_template("views/products/list-product.html")

@rootflaskapp.app.route("/products_add")
def products_add():
    return rootflaskapp.render_template("views/products/add-product.html")

@rootflaskapp.app.route("/products_edit")
def products_edit():
    return rootflaskapp.render_template("views/products/edit-product.html")