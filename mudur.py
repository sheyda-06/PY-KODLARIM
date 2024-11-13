class Çalısan:
    def __init__(self,isim,maas):
        self.isim=isim
        self.maas=maas

    def zamyap(self):
        return print(f"bu metod alt sınıfta tanımlanmalı")
    
class Mudur(Çalısan):

    def zamyap(self):
            return (self.maas*120)/100
    
class Iscı(Çalısan):
    def zamyap(self):
         return (self.maas*110)/100
    
a=Iscı("haydar",1000)
b=Mudur("suheda",90000)
print(a.zamyap())
print(b.zamyap())
