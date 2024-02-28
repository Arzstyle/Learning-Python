gaji_pokok = float(input("Masukan Gaji pokok karyawan : "))

#Elemen elemen
uang_transport_harian = 125_000
uang_makan_harian = 220_000
tunjangan_jabatan = 400_000
honor_lembur = 600_000

total_gaji = gaji_pokok + (uang_transport_harian + uang_makan_harian + tunjangan_jabatan + honor_lembur)

print(f"Total keseluruhan gaji karyawan adalah :{total_gaji: 1,.2f} rupiah.")
