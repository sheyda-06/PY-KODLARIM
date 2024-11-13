"""a=int(input("pozitif sayı giriniz:"))
x=0
while a>x:
    print(a)
    break
else:
    print("sayınız pozitif degil  pozitif bir sayı giriniz")"""



while True:
    sayı = int(input("Bir pozitif sayı girin (programdan çıkmak için negatif bir sayı girin): "))
    
    if sayı < 0:
        print("Bu sayı negatif, lütfen pozitif bir sayı girin.")
        continue  # Negatif bir sayı girildiğinde döngü başa döner ve tekrar input ister.
    
    print("Girilen sayı:", sayı)

