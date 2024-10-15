import rootflaskapp

@rootflaskapp.app.route('/orders_list')
def orders_list():
    return rootflaskapp.render_template('views/orders/list-order.html')

@rootflaskapp.app.route('/orders_add')
def orders_add():
    return rootflaskapp.render_template('views/orders/add-order.html')

@rootflaskapp.app.route('/orders_edit')
def orders_edit():
    return rootflaskapp.render_template('views/orders/edit-order.html')

@rootflaskapp.app.route('/orders_list_detail')
def orders_list_detail():
    return rootflaskapp.render_template('views/orders/list-order-detail.html')