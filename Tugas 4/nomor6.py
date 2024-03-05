# Buatlah program yang menghitung luas dan keliling segitiga berdasarkan panjang sisi-sisinya. (Gunakan Rumus Heron)

alas = int(input("Masukan Alas : "))
tinggi = int(input("Masukan Tinggi : "))

sisi_a = 12
sisi_b = 20
sisi_c = 16

rumus_luas = 1/2 * alas * tinggi
rumus_keliling_heron = (sisi_a + sisi_b + sisi_c) / 2

print(f"Hasil luas segitiga dengan alas {alas:.0f} cm dan tinggi {tinggi:.0f} cm adalah {rumus_luas} cm. ")
print(f"Hasil keliling menggunakan rumus heron {rumus_keliling_heron} cm. ")