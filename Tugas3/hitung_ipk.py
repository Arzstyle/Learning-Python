Algoritma = float(input(" Masukan Nilai Algoritma Anda : "))
PerancanganObjek = float(input(" Masukan Nilai Objek Anda : "))
Kalkulus = float(input(" Masukan Nilai Kalkulus Anda : "))
Etika = float(input(" Masukan Nilai Etika Anda : "))
ProfesiDatabase = float(input(" Masukan Nilai Database Anda : "))
English = float(input(" Masukan Nilai Inggris Anda : "))

def skorToBobot (skor):
    if skor >= 90:
        return 4
    elif skor >= 85:
        return 3.75
    elif skor >= 80:
        return 3.50
    elif skor >= 75:
        return 3.25
    elif skor >= 70:
        return 3
    elif skor >= 65:
        return 2.75
    elif skor >= 60:
        return 2.560
    elif skor >= 55:
        return 2.25
    elif skor >= 50:
        return 2
    elif skor >= 45:
        return 1.75
    elif skor >= 40:
        return 1.5
    elif skor >= 35:
        return 1.25
    elif skor >= 30:
        return 1
    else:
        return 0
    
nilai_mutu = 3

total_algoritma = nilai_mutu * skorToBobot(Algoritma)
total_objek = nilai_mutu * skorToBobot(PerancanganObjek)
total_kalkulus = nilai_mutu * skorToBobot(Kalkulus)
total_etika = nilai_mutu * skorToBobot(Etika)
total_database = nilai_mutu * skorToBobot(ProfesiDatabase)
total_english = nilai_mutu * skorToBobot(English)

total_mutu = nilai_mutu * 6 

total_ipk = (total_algoritma + total_objek + total_kalkulus + total_database + total_etika + total_english) / total_mutu

print(f" Nilai IPK anda adalah : {total_ipk:0,.2f} ")
  