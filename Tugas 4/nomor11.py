# Buatlah program untuk menghitung kelayakan orang lulus organisasi X. Organisasi X memiliki kriteria untuk Anggota
# 1. Perempuan dengan berat badan minimal 45kilo gram, maks 50 kilogram dan Tingginya minimal 165 cm dan Usianya kurang dari 20 tahun
# 2. Laki-laki dengan berat badan maks 70 kilo dan Tingginya minimal 170 cm dan usianya maks 25 tahun
# 3. Laki-laki dan Perempuan dengan nilai rata-rata Akademis 90 dan usianya kurang dari 30 tahun
# 4. Laki-laki dan Perempuan yang Memiliki Skill Menembak, Memanah atau Berkuda

# Ke 4 Kriteria diatas akan diterima hanya dan hanya jika tidak memiliki anggota tubuh yang cacat.

anggota_tubuh_cacat = input("Apakah bagian tubuh anda cacat? (ya/tidak) : " )

if anggota_tubuh_cacat == "ya": 
  print("Anda tidak lolos karena memiliki anggota tubuh yang cacat")
  exit()

jenis_kelamin = input("Masukan Jenis Kelamin Anda : ")
berat_badan = int(input("Masukan Berat Badan Anda : "))
tinggi_badan = int(input("Masukan Tinggi Badan Anda : "))
usia = int(input("Masukan Usia Anda : "))
nilai_akademis = int(input("Masukan Rata Rata Akademis : "))
have_skill = input("Apakah Anda Memiliki Skill? : ").split()


if any(skill in have_skill for skill in ["Menembak" , "Memanah", "Berkuda"]):
    print(f"Anda lulus kriteria 4!, berjenis kelamin {jenis_kelamin}, karena kamu memiliki skill {have_skill}.")
elif nilai_akademis  >= 90 and usia <= 30:
    print(f"Anda lulus Kriteria 3!, berjenis kelamin {jenis_kelamin}, dengan rata rata akademis : {nilai_akademis}, dan berusia {usia} Tahun.")
elif jenis_kelamin == "perempuan" and berat_badan >= 45 and berat_badan <= 50 and tinggi_badan >= 165 and usia <= 20:
    print(f"Anda Lulus Kriteria 1!, berjenis kelamin {jenis_kelamin}, dengan berat badan {berat_badan} kg, dan Tinggi {tinggi_badan}, dan berusia {usia}") 
elif jenis_kelamin == "laki laki" and berat_badan <= 70 and tinggi_badan >= 170 and usia <= 25: 
    print(f"Anda Lulus Kriteria 2!, berjenis kelamin {jenis_kelamin}, dengan berat badan {berat_badan} kg, dan Tinggi {tinggi_badan}, dan berusia {usia}") 
else:
    print("Maaf anda tidak lolos karena tidak memenuhi beberapa syarat")
  