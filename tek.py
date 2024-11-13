"""for i in range(1,1000):
    if i%2!=0:
        print(i)"""


"""a=int(input("sayıyı giriniz:"))
for i in range(1,a+1):
    if a%i==0:
        print(i)"""




yıl=int(input("yıl giriniz:"))
if (yıl %4==0 and yıl%100!=0) or (yıl %4==0 and  yıl %400==0):
    print("artık yıldır bu")
else:
    print("artık yıl degil")

a=input("metin giriniz:")
if a.isupper():
    print("metin tamamen buyuk")

elif a.islower():
    print("metin tamamen buyuk harflerden")

else:
    print("metin karma")

    






