import rootflaskapp

@rootflaskapp.app.route("/profile_view")
def profileview():
    return rootflaskapp.render_template("views/profile/view.html")

@rootflaskapp.app.route("/profile_edit")
def profileedit():
    return rootflaskapp.render_template("views/profile/edit.html")