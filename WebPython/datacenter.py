    #    c.execute("""CREATE TABLE IF NOT EXISTS khachhang (
    #         soCCCD TEXT PRIMARY KEY CHECK (length(soCCCD) = 12),
    #         ho TEXT NOT NULL CHECK (ho != ''),
    #         ten TEXT NOT NULL CHECK (ten != ''),
    #         email TEXT NOT NULL CHECK (email != ''),
    #         sdt TEXT NOT NULL CHECK (length(sdt) = 10),
    #         idBanglaixe TEXT NOT NULL CHECK (idBanglaixe != '' AND length(idBanglaixe) = 12)
    #     )""")
        
    #     c.execute("""CREATE TABLE IF NOT EXISTS phuongtien (
    #         so_dang_ki_xe TEXT PRIMARY KEY CHECK (length(so_dang_ki_xe) = 8),
    #         ten_phuong_tien TEXT NOT NULL CHECK (length(ten_phuong_tien) > 0),
    #         danh_muc TEXT NOT NULL  CHECK (length(danh_muc) > 0),
    #         so_cho_ngoi INTEGER NOT NULL CHECK (so_cho_ngoi > 0),
    #         tinh_trang_xe TEXT NOT NULL CHECK (tinh_trang_xe IN ('Sẵn sàng', 'Hết hàng')),
    #         gia_thue REAL NOT NULL CHECK (gia_thue > 0),
    #         loai_xe TEXT NOT NULL CHECK (loai_xe IN ('Sedan', 'SUV', 'Crossover', 'Convertible', 'Hatchback', 'Wagon', 'Van', 'Minivan', 'Coupe'))
    #     )""")
        
    #     c.execute("""CREATE TABLE IF NOT EXISTS donhang (
    #         masohoadon TEXT PRIMARY KEY CHECK (length(masohoadon) = 8),
    #         trangthaithanhtoan TEXT NOT NULL CHECK(trangthaithanhtoan IN ('Chưa thanh toán', 'Đã thanh toán')),
    #         thoigianbatdau TEXT NOT NULL,
    #         thoigianketthuc TEXT NOT NULL,
    #         soCCCD TEXT NOT NULL,
    #         so_dang_ky_xe TEXT NOT NULL,
    #         FOREIGN KEY(soCCCD) REFERENCES khachhang(soCCCD) ON DELETE CASCADE ON UPDATE CASCADE,
    #         FOREIGN KEY(so_dang_ky_xe) REFERENCES phuongtien(so_dang_ky_xe) ON DELETE CASCADE ON UPDATE CASCADE
    #     )""")