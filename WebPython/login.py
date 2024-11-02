import rootflaskapp
import email_automatic
emailAdmin = "admin"
passwordAdmin = "admin"

@rootflaskapp.app.route("/login_post", methods=["POST"])
def login_post():
    data = rootflaskapp.request.get_json()
    if data["email"] == emailAdmin and data["password"] == passwordAdmin:
        return rootflaskapp.redirect("/statistical")
    return rootflaskapp.jsonify("Login failed")

@rootflaskapp.app.route("/")
def login():
    return rootflaskapp.render_template("views/login.html")

@rootflaskapp.app.route("/testEmail")
def testEmail():
    email_automatic.send_email("n22dccn114@student.ptithcm.edu.vn", "0X1X256", "07/28/2004", "07/28/2100", "1000000", "Đã thanh toán", "Trần Đỗ Duy", "0123456789", "n22dccn114",  "Trần Ti Ni", "0123456789", "Exciter 150", "49AF12808", "Xe máy", "Yamaha", "100000")
    return rootflaskapp.jsonify("Test email")