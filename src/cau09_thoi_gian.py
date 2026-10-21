from datetime import datetime 
thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")
print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))
bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)
thoi_luong = ket_thuc - bat_dau
print(thoi_luong)
print(type(thoi_luong))
""" DU DOAN KET QUA
Khoang thoi gian: Tu 13:15 den 15:05 ngay 14/10/2026 la 1 gio 50 phut"""
""" SU KHAC NHAU GIUA datetime,str VA timedelta
datetime: bieu dien moc thoi gian cu the, ho tro thuc hien cac phep toan thoi gian
str: bieu dien thoi gian duoi dang chuoi ky tu van ban, khong the truc tiep thuc hien phep tinh toan thoi gian
timedelta: bieu dien do chenh lech giua hai moc thoi gian, khong gan voi mot moc ngay gio co dinh"""