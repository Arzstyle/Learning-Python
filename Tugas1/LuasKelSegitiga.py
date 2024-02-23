Alas = float(input ("Masukan Jumlah Alas : "))
Tinggi = float(input ("Masukan Jumlah Tinggi : "))

#Sisi setiap segitiga
sisiA = 17
sisiB = 12
sisiC = 10

rumusLuas = 1/2 * Alas * Tinggi
rumusKeliling = sisiA + sisiB + sisiC

print("Hasil perhitungan mencari Luas segitiga dengan 1/2 dikali Alas %.0f cm, dan Tinggi %.0f cm, adalah %.2f cm." %( Alas, Tinggi, rumusLuas))
print("Hasil perhitungan mencari Keliling segitiga dengan sisiA %.0f cm, ditambah sisiB %.0f cm, ditambah sisiC %.0f cm, adalah %.2f cm." %( sisiA, sisiB, sisiC, rumusKeliling)) 