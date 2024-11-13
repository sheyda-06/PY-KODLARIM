"""a=(input("metni giriniz:"))

for i in a:
    if i==" ":
        continue
    print(i,end="")"""


a=int(input("11 haneli tcnizi giriniz:"))
x=(a[0]+a[2]+a[4]+a[6]+a[8])*7
y=(a[1]+a[3]+a[5]+a[7])
c=x-y
c%10==a[9]
print(a[9])


