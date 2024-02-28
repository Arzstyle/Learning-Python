algoritma = 84
statistika = 85
pendidikanPancasila = 87
inggris = 88
kalkulus = 86
logikaInformatika = 90
organisasiKomputer = 85

def skorToBobot(skor):
  if skor >= 85:
    return 4.00
  elif skor >= 80:
    return 3.50
  elif skor >= 75:
    return 3.00
  elif skor >= 70:
    return 2.50
  else:
    return 2.00
  
  