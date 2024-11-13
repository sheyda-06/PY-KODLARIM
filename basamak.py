"""a=int(input("sayıyı giriniz:"))
kalan=a%10
y=(a-kalan)/10
if kalan>y:
    print(kalan)
    print(y)
elif kalan<y:
    print(y)
    print(kalan)"""




a = input("Sayı: ")  # Girdiyi alıyoruz, string olarak kalıyor

for i in a:
    for j in a:
        if i > j:
            print(f"{i} > {j}")


a=int(input("sayıyı giriniz:"))
kalan=a%10
a2=a//10
kalan2=a2%10
kalan3=a2//10
print(kalan3)
print(kalan2)
print(kalan)









        







