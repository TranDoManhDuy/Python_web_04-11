import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, receiver_email, subject, body, body_type = 'plain'):
    
    # tao doi tuong MIMEMultipart, chua thong tin email
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, body_type))
        
        # ket noi toi server SMTP cua Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        
        # gui email
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        
        # dong ket noi
        server.quit()
        print("Gui email thanh cong")
    except Exception as e:
        print(f"Da xay ra loi khi gui email: {e}")

# def main():
#     sender_email = "trandomanhduy2874@gmail.com"
#     sender_password = "gamw xsyj frri gsyf"
#     receiver_email = "n22dccn114@student.ptithcm.edu.vn"
#     subject = "Tieu de email"
#     body = "Noi dung email"
#     send_email(sender_email, sender_password, receiver_email, subject, body, 'plain')

# if __name__ == "__main__":
#     main()