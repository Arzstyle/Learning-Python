# Buatlah sebuah fungsi untuk menghitung keliling dan luas persegi panjang dengan menerima input panjang dan lebar.
# Contoh parameter: panjang = 5, lebar = 3
# Contoh output:
# luas 15, keliling 16

def kelilingLuas(p,l):
    keliling = 2 * (p + l)
    luas = p * l
    print(f"Luas : {luas}, Keliling : {keliling}")
    return luas, keliling

kelilingLuas(5,3)