import rootflaskapp

@rootflaskapp.app.route("/login")
def login():
    return rootflaskapp.render_template("views/login.html")