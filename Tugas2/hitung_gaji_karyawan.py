gaji_pokok = float(input("Masukan Gaji pokok karyawan : "))

#Elemen elemen
uang_transport_harian = 125.000
uang_makan_harian = 220.000
tunjangan_jabatan = 400.000
honor_lembur = 600.000

total_gaji = gaji_pokok + (uang_transport_harian + uang_makan_harian + tunjangan_jabatan + honor_lembur)

print(f"Total keseluruhan gaji karyawan adalah : {total_gaji: 1,.3f} rupiah.")
