# Kullanıcıdan metin girişi alma
gir = input("Metin giriniz: ")

# Girdi analizi için bayraklar
rakam_var = False
bosluk_var = False
ozel_karakter_var = False

# Özel karakterler için kontrol listesi
ozel_karakterler = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/"

# Girdiyi kontrol etme
for i in gir:
    if i.isdigit():
        rakam_var = True
    elif i.isspace():
        bosluk_var = True
    elif i in ozel_karakterler:
        ozel_karakter_var = True

# Sonuçları yazdırma
if rakam_var:
    print("Metin rakam içeriyor.")
if bosluk_var:
    print("Metin içinde boşluk var.")
if ozel_karakter_var:
    print("Metin özel karakter içeriyor.")
if not (rakam_var or bosluk_var or ozel_karakter_var):
    print("Metin sadece harflerden oluşuyor.")

