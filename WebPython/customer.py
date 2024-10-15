import rootflaskapp

@rootflaskapp.app.route('/customer_list')
def customer_list():
    return rootflaskapp.render_template('views/customer/list-customer.html')

@rootflaskapp.app.route('/customer_edit')
def customer_edit():
    return rootflaskapp.render_template('views/customer/edit-customer.html')

@rootflaskapp.app.route('/customer_add')
def customer_add():
    return rootflaskapp.render_template('views/customer/add-customer.html')