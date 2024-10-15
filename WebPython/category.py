import rootflaskapp

@rootflaskapp.app.route('/category_list')
def category_list():
    return rootflaskapp.render_template('views/categories/list-category.html')

@rootflaskapp.app.route('/category_add')
def category_add():
    return rootflaskapp.render_template('views/categories/add-category.html')

@rootflaskapp.app.route('/category_edit')
def category_edit():
    return rootflaskapp.render_template('views/categories/edit-category.html')