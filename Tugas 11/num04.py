# Tuliskan sebuah fungsi untuk menghitung jumlah elemen unik dalam sebuah daftar (list).
# Contoh parameter: my_list = [1, 2, 3, 3, 4, 4, 5]
# Contoh output: 5

def hitungElemen(my_list):
    return len(set(my_list))

print(hitungElemen([1, 2, 3, 3, 4, 4, 5]))