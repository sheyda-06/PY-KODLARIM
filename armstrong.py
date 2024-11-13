# Kullanıcıdan pozitif bir tam sayı alın
sayi = int(input("Bir pozitif tam sayı giriniz: "))

# Sayının string hali
sayi_str = str(sayi)

# Basamak sayısını bul
basamak_sayisi = len(sayi_str)

# Toplamı başlat
toplam = 0

# Her bir basamağı kontrol et
for i in sayi_str:
    # Basamağı tam sayıya çevir ve kuvvetini al
    toplam += int(i) ** basamak_sayisi

# Sonucu kontrol et
if toplam == sayi:
    print(f"{sayi} bir Armstrong sayısıdır.")
else:
    print(f"{sayi} bir Armstrong sayısı değildir.")

