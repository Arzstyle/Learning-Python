tahunSekarang = 2024

Nama = input("Masukan Nama Anda : ")
tempatLahir = input("Masukan Tempat Lahir Anda : ")
tanggalLahir = float(input("Masukan Tanggal Lahir Anda : "))
tahunLahir = float(input("Masukan Tahun Lahir Anda : "))
nilaiEnglish = float(input("Masukan Nilai English : "))
nilaiMtk = float(input("Masukan Nilai MTK : "))
nilaiIndonesia = float(input("Masukan Nilai Indonesia : "))
jenisKelamin = input("Masukan Jenis Kelamin Anda : ")

rataRata = (nilaiEnglish + nilaiIndonesia + nilaiMtk) / 3
umur = tahunSekarang - tahunLahir

if umur >= 24:
  print("Umur anda melebihi batas pendaftaran")
elif rataRata >= 80 and jenisKelamin == "laki laki":
  print(f"Dengan rata rata : {rataRata:.2f} dan berjenis kelamin {jenisKelamin} disarankan masuk Jurusan Teknik Informatika ")
elif rataRata >= 80 and jenisKelamin == "Perempuan":
  print(f"Dengan rata rata : {rataRata:.2f} dan berjenis kelamin {jenisKelamin} disarankan masuk Jurusan Sistem Informasi ")
else:
  print("Silahkan masuk Jurusan DKV") 

  

