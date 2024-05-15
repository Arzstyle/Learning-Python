# Buatlah sebuah fungsi untuk mengecek apakah sebuah string adalah palindrom atau tidak.
# Contoh parameter: kata = "level"
# Contoh output: "level adalah palindrom"

def cek_palindrom(kata):
    
    kata = kata.lower()
    
    if kata == kata[::-1]:
        return f"{kata} adalah palindrom"
    else:
        return f"{kata} bukan palindrom"
        
print(cek_palindrom("level"))

    
    