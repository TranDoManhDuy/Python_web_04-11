import rootflaskapp

emailAdmin = "admin"
passwordAdmin = "admin"

@rootflaskapp.app.route("/login_post", methods=["POST"])
def login_post():
    data = rootflaskapp.request.get_json()
    print(data)
    if data["email"] == emailAdmin and data["password"] == passwordAdmin:
        return rootflaskapp.redirect("/statistical")
    return rootflaskapp.jsonify("Login failed")

@rootflaskapp.app.route("/")
def login():
    return rootflaskapp.render_template("views/login.html")