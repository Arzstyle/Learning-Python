# Tuliskan program untuk menentukan bilangan itu bilangan positif, negatif atau 0

bilangan = int(input("Masukan Bilangan : "))

if bilangan == 0:
    print(f"{bilangan} adalah bilangan netral")
elif bilangan > 0:
    print(f"{bilangan} adalah bilangan positif")
else: 
    print(f"{bilangan} adalah bilangan negatif")