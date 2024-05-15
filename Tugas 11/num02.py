# Buatlah sebuah fungsi untuk menambahkan semua angka dalam sebuah list dan mengembalikan hasilnya.
# Contoh parameter: my_list = [1, 2, 3, 4, 5]
# Contoh output: 15

def menambahkan(my_list):
    total = 0
    for angka in my_list:
        total += angka
    return total

print(menambahkan([1, 2, 3, 4, 5]))