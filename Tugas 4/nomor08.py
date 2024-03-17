#Program yang mensimulasikan permainan batu-gunting-kertas antara dua pemain dan menentukan pemenangnya.

p1 = input("Player 1 memilih : ")
com = input("Computer memilih : ")

pick_1 = "batu"
pick_2 = "gunting" 
pick_3 = "kertas"

if p1 == pick_1 and com == pick_2:
  print(f"Player 1 menang")
elif p1 == pick_2 and com == pick_1:
  print(f"Player 2 menang")
elif p1 == pick_1 and com == pick_3:
  print(f"Player 2 menang")
elif p1 == pick_3 and com == pick_1:
  print(f"Player 1 menang")
elif p1 == pick_2 and com == pick_3:
  print(f"Player 1 menang")
elif p1 == pick_3 and com == pick_2:
  print(f"Player 2 menang")
else:
  print(f"Hasil seimbang")