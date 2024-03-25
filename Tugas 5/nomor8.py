a, b, c = 1, 2, 3

print(a, b, c, end=" ")

for i in range(7):
  d = a + b + c
  print(d, end=" ")
  a = b
  b = c
  c = d
  
print()

