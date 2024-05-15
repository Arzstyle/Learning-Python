# Buatlah sebuah fungsi untuk mengurutkan sebuah string dalam urutan alfabetik.
# Contoh parameter: string = "python"
# Contoh output: "hnopty"

def mengurutkan(string):
    return ''.join(sorted(string))

print(mengurutkan("python"))