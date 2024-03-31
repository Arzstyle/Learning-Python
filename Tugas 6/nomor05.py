for i in range(5, 0, -1):
    for j in range(1, 6):
        print("_" if j < i else j, end=" ")
    print()