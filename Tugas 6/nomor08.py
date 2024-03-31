a, b = 1, 1

for i in range(7): 
    print("* " * a)
    a, b = b, a + b
    # c = b
    # b = a + b
    # a = c 
print()