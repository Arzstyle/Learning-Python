# Diketahui Harga laptop Zaid Abdullah adalah 39.000.000, dengan masa manfaat 7 tahun dan 
# nilai sisa setelah 7 tahun di perkirakan sebesar 4.000.000. 
# Berapakah Nilai Aset Laptop Bapak Zaid Abdullah setelah 3 tahun?

# SusutTahunan = (39.000.000-4.000.000)/7 = 5.000.000
# Masa Pakai 3 tahun, berarti harga laptop sudah menyusut 5.000.000*3 = 15.000.000
# Nilai Aset Tersisa adalah 39.000.000 - 15.000.000 = 24.000.000
# keterangan : Harga beli, Masa manfaat dan perkiraan nilai sisa setelah masa manfaat habis tiap barang berbeda-beda. 
# Buatlah kalkulator untuk mengakomodasi kasus diatas

harga_laptop = int(input("Masukan Harga Laptop : "))
nilai_sisa = int(input("Masukan Nilai Sisa : "))
masa_manfaat = int(input("Masa Tahunan Laptop : "))

susut_tahunan = (harga_laptop - nilai_sisa)/masa_manfaat
masa_pakai = susut_tahunan * 3
nilai_aset_tersisa = harga_laptop - masa_pakai

print(f"Harga beli laptop adalah : {harga_laptop}")
print(f"Nilai Sisa : {nilai_sisa}")
print(f"Masa Manfaat : {masa_manfaat}")
print(f"Susut Tahunan : {susut_tahunan}")
print(f"Masa Pakai 3 tahun penggunaan : {masa_pakai} ")
print(f"Nilai Aset Tersisa adalah : {nilai_aset_tersisa}")


