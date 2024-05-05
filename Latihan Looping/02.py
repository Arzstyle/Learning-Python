name = "SUKABUMII"

for i in range(9):
    for j in range(len(name)):
        if j>=i-1 and j<10-i:
            print(name[j], end=" ")
        else:
            print("*", end=" ")
    print()