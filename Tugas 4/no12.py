tahun_sekarang = 2024

anggota_tubuh_cacat = input("Apakah anda memiliki anggota tubuh cacat ? ")
jenis_kelamin = input("Masukkan jenis kelamin :")
berat_badan = int(input("Masukkan berat badan :"))
tinggi_badan = int(input("Masukkan tinggi badan :"))
tahun_lahir = int(input("Masukkan tahun lahir :"))
nilai_akademis = int(input("Masukkan nilai akademis :"))
skill = input("Masukkan Skill :")

usia = tahun_sekarang - tahun_lahir

if anggota_tubuh_cacat == "memiliki":
  print(f"Anda tidak memenuhi kriteria karena memilik anggota tubuh cacat")
else:
  if jenis_kelamin == "perempuan" and berat_badan >= 45:
    if berat_badan <= 50 and tinggi_badan >= 165 and usia <= 20:
      print(f"Anda memenuhi kriteria 1")
    else:
      print(f"Anda tidak memenuhi kriteria 1")
  if jenis_kelamin == "laki laki" and berat_badan <= 70:
    if tinggi_badan >= 170 and usia <= 30:
      print(f"Anda memenuhi kriteria 2")
    else:
      print(f"Anda tidak memenuhi kriteria 2")
  if jenis_kelamin == "laki laki" or jenis_kelamin == "perempuan":
    if nilai_akademis >= 90 and usia <= 30:
      print(f"Anda memnuhi kriteria 3")
    else:
      print(f"Anda tidak memnuhi kriteria 3")
  if jenis_kelamin == "laki laki" or jenis_kelamin == "perempuan":
    if skill == "menembak" or skill == "memanah" or skill == "berkuda":
      print(f"Anda memenuhi kriteria 4")
    else:
      print(f"anda tidak memenuhi kriteria 4")