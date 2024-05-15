uangBelanja = float (input (" Masukan uang belanja : "))
totalBarang = float (input(" Masukan total barang : "))

kembalian = uangBelanja - totalBarang 

if totalBarang > 70.000:
    diskon = totalBarang * (10/100)
    kembalian += diskon
    print(f"Sisa kembalian anda dengan diskon adalah : {kembalian:1,.2f} rupiah")
else: 
    print(f"Sisa kembalian anda tanpa diskon adalah : {kembalian:1,.2f} rupiah")
    
    