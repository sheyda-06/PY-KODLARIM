# Kullanıcıdan dört sayı alma
a = int(input("Sayı1: "))
b = int(input("Sayı2: "))
c = int(input("Sayı3: "))
d = int(input("Sayı4: "))

# Sayıları listeye ekleme
liste = []
liste.append(a)
liste.append(b)
liste.append(c)
liste.append(d)
print("Girdiğiniz sayılar:", liste)

# Bayraklar
pozitif_var = True
negatif_var = True
sifir_var = False

# Listeyi kontrol etme
for i in liste:
    if i > 0:
        negatif_var = False
    elif i < 0:
        pozitif_var = False
    elif i == 0:
        sifir_var = True

# Sonuçları yazdırma
if pozitif_var and not sifir_var and not negatif_var:
    print("Hepsi pozitif.")
elif negatif_var and not sifir_var and not pozitif_var:
    print("Hepsi negatif.")
elif sifir_var:
    print("Dizi sıfır sayısını içeriyor.")
else:
    print("Dizi hem pozitif hem de negatif sayılar içeriyor.")
