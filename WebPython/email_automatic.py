import rootflaskapp
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import locale

def send_email(receiver_email, 
               MA_SO_HOA_DON, 
               NGAY_BAT_DAU, 
               NGAY_KET_THUC, 
               TONG_TIEN, 
               TRANG_THAI, 
               TEN_KHACH_HANG, 
               SDT_KHACH_HANG, 
               MA_SO_NHAN_VIEN_BAN_HANG, 
               TEN_NHAN_VIEN_BAN_HANG, 
               SDT_NHAN_VIEN_BAN_HANG, 
               TEN_PHUONG_TIEN, 
               SO_DANG_KY, 
               LOAI_PHUONG_TIEN, 
               DANH_MUC, 
               GIA_THUE):
    # tạo ra đối tượng MINEutipart để chứa email
    
    # body = render_template('email.html', data = dict) email.html là cấu trúc mail đặt trong templates, data la du lieu truyen vao dạng dict
    # type = 'html' để hiển thị đúng cấu trúc mail
    try:
        locale.setlocale(locale.LC_ALL, 'vi_VN.UTF-8')
        emailMsg = MIMEMultipart()
        emailMsg['From'] = "trandomanhduy2874@gmail.com"
        emailMsg['To'] = receiver_email
        emailMsg['Subject'] = "Hóa đơn dịch vụ đăng kí thuê xe VNTHACO!!!"
        
        body = rootflaskapp.render_template('email.html', 
                                            MA_SO_HOA_DON = MA_SO_HOA_DON, 
                                            NGAY_BAT_DAU = NGAY_BAT_DAU, 
                                            NGAY_KET_THUC = NGAY_KET_THUC, 
                                            TONG_TIEN = TONG_TIEN, 
                                            TRANG_THAI = TRANG_THAI, 
                                            TEN_KHACH_HANG = TEN_KHACH_HANG, 
                                            SDT_KHACH_HANG = SDT_KHACH_HANG, 
                                            EMAIL_KHACH_HANG = receiver_email, 
                                            MA_SO_NHAN_VIEN_BAN_HANG = MA_SO_NHAN_VIEN_BAN_HANG, 
                                            TEN_NHAN_VIEN_BAN_HANG = TEN_NHAN_VIEN_BAN_HANG, 
                                            SDT_NHAN_VIEN_BAN_HANG = SDT_NHAN_VIEN_BAN_HANG, 
                                            TEN_PHUONG_TIEN = TEN_PHUONG_TIEN, 
                                            SO_DANG_KY = SO_DANG_KY, 
                                            LOAI_PHUONG_TIEN = LOAI_PHUONG_TIEN, 
                                            DANH_MUC = DANH_MUC, 
                                            GIA_THUE = locale.currency(float(GIA_THUE), grouping=True))
        emailMsg.attach(MIMEText(body, "html"))
        
        # ket noi toi server SMTP cua Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login( "trandomanhduy2874@gmail.com", "gamw xsyj frri gsyf")
        
        # gui email
        text = emailMsg.as_string()
        server.sendmail( "trandomanhduy2874@gmail.com", receiver_email, text)
        
        # dong ket noi
        server.quit()
        print("Gui email thanh cong")
    except Exception as e:
        print(f"Da xay ra loi khi gui email: {e}")