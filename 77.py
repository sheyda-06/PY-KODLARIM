class Calisan:
    def __init__(self, isim, maas):
        self.isim = isim
        self.maas = maas

    def zam_yap(self):
        print("Bu metod alt sınıfta tanımlanmalı!")


class Mudur(Calisan):
    def zam_yap(self):
        self.maas = (self.maas * 120) / 100  # %20 zam yapılıyor
        return self.maas


class Isci(Calisan):
    def zam_yap(self):
        self.maas = (self.maas * 110) / 100  # %10 zam yapılıyor
        return self.maas


# Nesneleri oluşturup zam yapma işlemlerini test edelim
isci = Isci("Haydar", 1000)
mudur = Mudur("Ahmet", 10000)

print(f"{isci.isim}'in yeni maaşı: {isci.zam_yap()}")  # Haydar için zam yapılmış maaşı yazdırır
print(f"{mudur.isim}'in yeni maaşı: {mudur.zam_yap()}")  # Ahmet için zam yapılmış maaşı yazdırır
