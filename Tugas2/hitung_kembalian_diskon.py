uangBelanja = float (input (" Masukan uang belanja : "))
totalBarang = float (input(" Masukan total barang : "))

if totalBarang > 70.000:
    diskon = totalBarang * (10/100)
    print(f"Sisa kembalian anda dengan diskon adalah : {diskon:0.3f} rupiah")
else: diskon = 0

totalBelanja = uangBelanja - totalBarang + diskon
print(f"Sisa kembalian adalah : {totalBelanja:0.3f} rupiah")
    
    