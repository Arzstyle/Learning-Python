# Tulisan program yang meminta input 3 buah bilangan dan tentukan bilangan mana yang lebih kecil

bilangan_1 = int(input("Masukan Bilangan 1 : "))
bilangan_2 = int(input("Masukan Bilangan 2 : "))
bilangan_3 = int(input("Masukan Bilangan 3 : "))

if bilangan_1 < bilangan_2 and  bilangan_1 < bilangan_3:
    print(f"Benar karena bilangan {bilangan_1} lebih kecil dari {bilangan_2} dan {bilangan_3} ")
elif bilangan_2 < bilangan_1 and bilangan_2 < bilangan_3: 
    print(f"Benar karena bilangan {bilangan_2} lebih kecil dari {bilangan_1} dan {bilangan_3}  ")
elif bilangan_3 < bilangan_1 and bilangan_3 < bilangan_2: 
    print(f"Benar karena bilangan {bilangan_3} lebih kecil dari {bilangan_1} dan {bilangan_2} ")
else :
    print(f"Ketiga bilangan sama besar")