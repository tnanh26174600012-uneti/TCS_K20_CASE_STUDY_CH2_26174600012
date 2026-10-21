tong_phut = 135
cong_suat_w = 250
so_gio = tong_phut // 60
so_phut_du = tong_phut % 60
print(f"So gio tron ven: {so_gio} gio")
print(f"So phut con lai: {so_phut_du} phut")
su_dung_lau = tong_phut > 60
print("Su dung lau:", su_dung_lau)
du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)
print("Du lieu hop le:", du_lieu_hop_le)

#DU DOAN
# 100 + 20 * 3 = 100 + 60 = 160
# (100 + 20) * 3 = 120 * 3 = 360
phep_tinh_1 = 100 + 20 * 3
phep_tinh_2 = (100 + 20) * 3
print("Phep tinh 1:", phep_tinh_1)
print("Phep tinh 2:", phep_tinh_2)
