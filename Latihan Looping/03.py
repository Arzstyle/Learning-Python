name = "SUKABUMII"

for i in range(8, -1, -1):
    for j in range(len(name)):
        if i+j-8:
            print(name[j], end=" ")
        else:
            print("*", end=" ")
    print()