# Buatlah program untuk menghitung kelayakan orang lulus organisasi X. Organisasi X memiliki kriteria untuk Anggota
# 1. Perempuan dengan berat badan minimal 45kilo gram, maks 50 kilogram dan Tingginya minimal 165 cm dan Usianya kurang dari 20 tahun
# 2. Laki-laki dengan berat badan maks 70 kilo dan Tingginya minimal 170 cm dan usianya maks 25 tahun
# 3. Laki-laki dan Perempuan dengan nilai rata-rata Akademis 90 dan usianya kurang dari 30 tahun
# 4. Laki-laki dan Perempuan yang Memiliki Skill Menembak, Memanah atau Berkuda

# Ke 4 Kriteria diatas akan diterima hanya dan hanya jika tidak memiliki anggota tubuh yang cacat.

berat_badan = int(input("Masukan Berat Badan Anda : "))
tinggi_badan = int(input("Masukan Tinggi Badan Anda : "))
usia = int(input("Masukan Umur Anda : "))
jenis_kelamin = input("Masukan Jenis Kelamin Anda : ")
rata_rata = int(input("Masukan Rata Rata Akademis : "))
skill = input("Apakah Anda Memiliki Skill? : ")

kecacatan = True or False

if kecacatan == False: 
  print("Anda Tidak Lolos karena tidak memenuhi kritea anggota Tubuh")
elif (jenis_kelamin == "Laki laki" or jenis_kelamin == "Perempuan") and rata_rata >= 90 and usia <= 30:
  print(f"Selamat Anda Lulus!, Anda bejernis kelamin {jenis_kelamin}, dengan rata rata akademis {rata_rata}, dan berusia {usia} Tahun.")
elif jenis_kelamin == "Perempuan" and berat_badan >= 45 and berat_badan <= 50 and tinggi_badan >= 165 and usia <= 20: 
  print(f"Selamat Anda Lulus!, Anda bejernis kelamin {jenis_kelamin}, dengan berat badan {berat_badan} kg, dan Tinggi {tinggi_badan}, dan berusia {usia} Tahun.")
elif jenis_kelamin == "Laki laki" and berat_badan <= 70 and tinggi_badan >= 170 and usia <= 25:
  print(f"Selamat Anda Lulus!, Anda bejernis kelamin {jenis_kelamin}, dengan berat badan {berat_badan} kg, dan Tinggi {tinggi_badan}, dan berusia {usia} Tahun.")
elif (jenis_kelamin == "Laki Laki" or jenis_kelamin == "Perempuan") and skill == "Menembak" or skill == "Memanah" or skill == "Berkuda":
  print(f"Selamat Anda Lulus!, Anda bejernis kelamin {jenis_kelamin}, karena kamu memiliki skill {skill}.")
else:
  print("Nilai yang anda masukan tidak sesuai dengan kritea yang di inginkan.")