import rootflaskapp
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, receiver_email, subject, body, body_type = 'plain'):
    # tạo ra đối tượng MINEutipart để chứa email
    
    # body = render_template('email.html', data = dict) email.html là cấu trúc mail đặt trong templates, data la du lieu truyen vao dạng dict
    # type = 'html' để hiển thị đúng cấu trúc mail
    try:
        emailMsg = MIMEMultipart()
        emailMsg['From'] = sender_email
        emailMsg['To'] = receiver_email
        emailMsg['Subject'] = subject
        
        emailMsg.attach(MIMEText(body, body_type))
        
        # ket noi toi server SMTP cua Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        
        # gui email
        text = emailMsg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        
        # dong ket noi
        server.quit()
        print("Gui email thanh cong")
    except Exception as e:
        print(f"Da xay ra loi khi gui email: {e}")
        
def test():
    sender_email = "trandomanhduy2874@gmail.com"
    sender_password = "gamw xsyj frri gsyf"
    receiver_email = "n22dccn114@student.ptithcm.edu.vn"
    subject = "Hoa don cua ban"
    body = rootflaskapp.render_template('email.html', data = {"name": "Duy", "age": 20}, message="Hello World!")
    body_type = "html"
    send_email(sender_email, sender_password, receiver_email, subject, body, body_type)