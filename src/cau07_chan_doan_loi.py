ma_may = input("Nhap ma may: ")
cong_suat_w = float(input("Nhap cong suat W: "))
so_phut = int(input("Nhap so phut: "))
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"May: {ma_may}")
print(f"Dien nang: {dien_nang_kwh:.3f} kWh")
#LOI
#1. cau07_chan_doan_loi.py, dong 6, SyntaxError: '(' was never closed
#Nguyen nhan: thieu dau ngoac dong cuoi lenh print()
#2. cau07_chan_doan_loi.py, dong 4, TypeError: unsupported operand type(s) for /: 'str' and 'int'
#Nguyen nhan: Bien cong_suat_w chua ep kieu float/int nen co kieu str, dan den khong the thuc hien phep chia voi so nguyen o dong 4
#3. cau07_chan_doan_loi.py, dong 6, NameError: name 'dien_nang' is not defined
#Nguyen nhan: Goi ten dien_nang khong ton tai