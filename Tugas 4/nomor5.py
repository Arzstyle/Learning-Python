# Tuliskan program untuk menentukan bilangan itu bilangan (ganjil/genap) positif, negatif atau 0

bilangan = int(input("Masukan Bilangan : "))

if bilangan > 0 and bilangan %2 == 0:
    print(f"{bilangan} adalah bilangan positif dan genap")
elif bilangan > 0 and bilangan %2 == 1:
    print(f"{bilangan} adalah bilangan positif dan ganjil")
elif bilangan < 0 and bilangan %2 == 0:
    print(f"{bilangan} adalah bilangan negatif dan genap")
elif bilangan < 0 and bilangan %2 == 1:
    print(f"{bilangan} adalah bilangan negatif dan ganjil")
else:
    print(f"{bilangan} adalah bilangan netral atau")