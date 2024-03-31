a = 1
b = 1
c = 2

for i in range(5):
  a = b
  for j in range(5):
    print(a, end=" ")
    a += c
  b += 1
  c += 1
  print()