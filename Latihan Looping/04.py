name = "SUKABUMIISUKABUMII"

for i in range(9):
    for j in range(len(name)):
        if j >= 8 - i and j <= 8 + i:
            print(name[j], end=" ")
        else:
            print("*", end=" ")
    print()
    
for i in range(8, -1, -1):
    for j in range(len(name)):
        if j >= 8 - i and j <= 8 + i:
            print(name[j], end=" ")
        else:
            print("*", end=" ")
    print()

for i in range(9):
    for j in range(len(name)):
        if i+j-8 and i+j-16:
            print(name[j], end=" ")
        else:
            print("*", end=" ")
    print()
    
for i in range(8, -1, -1):
    for j in range(len(name)):
        if i+j-8 and i+j-16:
            print(name[j], end=" ")
        else:
            print("*", end=" ")
    print()