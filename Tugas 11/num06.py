# Tuliskan sebuah fungsi untuk menghitung jumlah kata dalam sebuah kalimat.
# Contoh parameter: kalimat = "Ini adalah contoh kalimat"
# Contoh output: 4

def jumlahKata(kalimat):
    kata_kalimat = kalimat.split()
    return len(kata_kalimat)

print(jumlahKata("ini adalah contoh kalimat"))
