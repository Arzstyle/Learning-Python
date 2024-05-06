name = "SUKABUMIISUKABUMII"

for i in range(6):
    for j in range(len(name)):
        if j > i - 2:
            print(name[j], end=" ")
        else:
            print("*", end=" ")
    print()
    
for i in range(5, -1, -1):
    for j in range(len(name)):
        if j > i + 7:
            print(name[j], end=" ")
        else:
            print("*", end=" ")
    print()