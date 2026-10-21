cong_suat_w = 250
so_phut = 60
don_gia_kwh = 3000
dien_nang_kwh = cong_suat_w * so_phut /60 /1000
chi_phi = dien_nang_kwh * don_gia_kwh
print("Dien nang tieu thu:", dien_nang_kwh, "kWh | Kieu du lieu:", type(dien_nang_kwh))
print("Chi phi dien:", chi_phi, "VND | Kieu du lieu:", type(chi_phi))
#Du doan 1
# Dien nang tieu thu: 0.375 kWh
# Chi phi dien: 1125.0 VND
#Du doan 2
#Dien nang tieu thu: 0.25 kWh
#Chi phi dien: 750.0 VND
