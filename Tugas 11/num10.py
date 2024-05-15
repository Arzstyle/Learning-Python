# Buatlah sebuah fungsi untuk menentukan apakah suatu kata adalah anagram atau tidak.
# Contoh parameter: kata1 = "listen", kata2 = "silent"
# Contoh output: True

def cek_anagram(kata1, kata2):
    
    sorted_kata1 = sorted(kata1)
    sorted_kata2 = sorted(kata2)
   
    if sorted_kata1 == sorted_kata2:
        return True
    else:
        return False
    
print(cek_anagram("listen", "silent"))

