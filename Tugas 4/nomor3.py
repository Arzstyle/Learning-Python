# Tuliskan program yang meminta input 3 buah bilangan dan tentukan bilangan mana yang lebih besar, 2 bilangan lebih besar dari yang lain atau semua bilangan sama besar

a = int(input("Masukan Bilangan 1 : "))
b = int(input("Masukan Bilangan 2 : "))
c = int(input("Masukan Bilangan 3 : "))

if a > b and a > c:
    print(f"bilangan a {a} lebih besar dibanding {b} dan {c}")
elif b > a and b > c:
    print(f"bilangan b {b} lebih besar dibanding {a} dan {c}")
elif c > a and c > b:
    print(f"bilangan c {c} lebih besar dibanding bilangan a : {a} dan bilangan b : {b}.")
    
elif a == b > c:
    print(f"bilangan a : {a}, sama dengan bilangan b : {b}, tapi lebih besar dari bilnagan c : {c}.")
elif b == a and c:
    print(f"bilangan b : {b}, sama dengan bilangan a : {a}, tapi lebih besar dari bilangan c : {c}.")
elif c == a > b:
    print(f"bilangan c : {c}, sama dengan bilangan a : {a}, tapi lebih besar dari bilangan b : {b}.")
else :
    print(f"bilangan a : {a}, bilangan b : {b} dan bilangan c : {c} sama besar. ")
