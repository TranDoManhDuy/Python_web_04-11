import rootflaskapp

@rootflaskapp.app.route("/list_users")
def list_user():
    return rootflaskapp.render_template("views/users/list-user.html")

@rootflaskapp.app.route("/edit_user")
def edit_user():
    return rootflaskapp.render_template("views/users/edit-user.html")

@rootflaskapp.app.route("/add_user")
def add_user():
    return rootflaskapp.render_template("views/users/add-user.html")