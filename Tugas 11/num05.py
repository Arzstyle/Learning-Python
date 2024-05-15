# Buatlah sebuah fungsi untuk menghitung nilai faktorial dari sebuah bilangan bulat.
# Contoh parameter: n = 5
# Contoh output: 120

def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)
    
print(faktorial(5))


# Menggunakan For
# def faktorial(n):
#     hasil = 1
#     for i in range(1, n + 1):
#         hasil *= i
#     return hasil

# nilai = 5
# hasil = faktorial(nilai)
# print(hasil)


