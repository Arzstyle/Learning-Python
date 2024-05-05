name = "SUKABUMII"

for i in range(9):
    for j in range(len(name)):
        if(j<i+1):
            print(name[j], end=" ")
        else:
            print("*", end=" ")
    print()
