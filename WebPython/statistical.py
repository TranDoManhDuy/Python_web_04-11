import rootflaskapp

@rootflaskapp.app.route("/statistical")
def statistical():
    return rootflaskapp.render_template("views/statistical/statistical.html")