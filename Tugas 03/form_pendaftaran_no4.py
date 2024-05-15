tahun_sekarang = 2024

nama = input("Masukan Nama Anda : ")
tempat_lahir = input("Masukan Tempat Lahir Anda : ")
tanggal_lahir = float(input("Masukan Tanggal Lahir Anda : "))
tahun_lahir = float(input("Masukan Tahun Lahir Anda : "))
nilai_english = float(input("Masukan Nilai English : "))
nilai_mtk = float(input("Masukan Nilai MTK : "))
nilai_indonesia = float(input("Masukan Nilai Indonesia : "))
jenis_kelamin = input("Masukan Jenis Kelamin Anda : ")

rataRata = float(nilai_english + nilai_indonesia + nilai_mtk) / 3
umur = tahun_sekarang - tahun_lahir

if umur >= 25:
  print(f"Umur anda yaitu {umur} tahun, melebihi batas umur pendaftaran yang telah ditentukan.")
elif rataRata >= 80:
    if jenis_kelamin == "laki laki":
       jurusan = "Teknik Informatika"
       print(f"{nama}, Selamat! Dengan nilai rata rata : {rataRata:.2f}, dan berjenis kelamin {jenis_kelamin}, Anda disarankan masuk Jurusan Teknik Informatika. ")
    elif jenis_kelamin == "Perempuan":
       jurusan = "Sistem Informasi"
       print(f"{nama}, Selamat! Dengan nilai rata rata : {rataRata:.2f}, dan berjenis kelamin {jenis_kelamin}, Anda disarankan masuk Jurusan Sistem Informasi. ")
    else:
      print("Mohon maaf Jurusan yang disarankan tidak diketahui karena jenis kelamin tidak valid. ")
else:
  print(f"Maaf, nilai rata rata anda tidak mencapai, yaitu {rataRata}, Jadi anda disarankan masuk jurusan DKV")
