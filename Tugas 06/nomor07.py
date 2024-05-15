for i in range(5, 0, -1):
    for j in range(i):
        if (i + j) % 2 != 0:
            print("S", end=" ")
        if (i + j) % 2 == 0:
            print("O", end=" ")
    print()