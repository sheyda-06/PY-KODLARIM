import random

# Olası kelimeler listesi
kelimeler = ["python", "bilgisayar", "oyun", "yazılım", "internet"]

# Rastgele kelime seçimi
secili_kelime = random.choice(kelimeler)
gizli_kelime = ["_" for _ in secili_kelime]  # Kelimeyi gizlemek için

tahmin_hakki = 6  # Oyuncunun toplamda 6 yanlış tahmin hakkı var
yanlis_tahminler = []

print("Kelime Tahmin Oyununa Hoşgeldiniz!")
print(f"Kelime: {' '.join(gizli_kelime)}")

# Oyun döngüsü
while tahmin_hakki > 0 and "_" in gizli_kelime:
    tahmin = input("Bir harf tahmin edin: ").lower()

    if len(tahmin) != 1 or not tahmin.isalpha():
        print("Lütfen geçerli bir harf girin.")
        continue

    if tahmin in yanlis_tahminler or tahmin in gizli_kelime:
        print("Bu harfi zaten tahmin ettiniz.")
        continue

    if tahmin in secili_kelime:
        # Doğru tahmin
        for i, harf in enumerate(secili_kelime):
            if harf == tahmin:
                gizli_kelime[i] = tahmin
        print(f"Doğru! Kelime: {' '.join(gizli_kelime)}")
    else:
        # Yanlış tahmin
        tahmin_hakki -= 1
        yanlis_tahminler.append(tahmin)
        print(f"Yanlış! Kalan tahmin hakkı: {tahmin_hakki}")

# Oyun sonu durumu
if "_" not in gizli_kelime:
    print(f"Tebrikler! Kelimeyi buldunuz: {secili_kelime}")
else:
    print(f"Maalesef, tahmin hakkınız bitti. Kelime: {secili_kelime}")
