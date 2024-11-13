
# Kullanıcıdan kelime girişi alma
girdi = input("Kelime girin (boşlukla ayırarak): ")

# Boş dizi kontrolü
if not girdi:
    print("Hiç kelime girmediniz.")
else:
    # Girilen kelimeleri listeye dönüştürme
    kelimeler = girdi.split()


