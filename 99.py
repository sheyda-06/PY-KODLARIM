class Çalısan:
    def __init__(self,ad ,maas):
        self.ad=ad
        self.maas=maas

    def maasarttır(self,arttır):
        self.maas+=arttır
        return self.maas
    
class Yönetici(Çalısan):
    def __init__(self,ad,maas):
        super().__init__(ad,maas)

    def göster(self,çalısansayı):
        print(f"çalışan sayısı=={çalısansayı}")

    def bilgigöster(self):
        print(f"adı={self.ad},maas={self.maas}")


a=Çalısan("suheda",10)
b=Yönetici("haydar",40)
print(a.maasarttır(1))
print(b.bilgigöster())







