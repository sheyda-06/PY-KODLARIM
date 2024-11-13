class Şekil:
    def __init__(self):
        return (f"bu metod alt sınıfta tanımlanmalı")

    def alan(self):
         return ("Bu metod alt sınıfta tanımlanmalı!")

    def cevre(self):
        return ("Bu metod alt sınıfta tanımlanmalı!")



class Dikdörtgen(Şekil):
    def __init__(self,uzunluk,genişlik):
        super().__init__()
        self.uzunluk=uzunluk
        self.genişlik=genişlik

    def alan(self):
        return self.uzunluk * self.genişlik

    def cevre(self):
        return 2 * (self.uzunluk + self.genişlik)


class Kare(Şekil):
    def __init__(self,kenar):
        super().__init__()
        self.kenar=kenar




    def alan(self):
        return self.kenar ** 2  # Kare alanı kenarın karesi

    def cevre(self):
        return 4 * self.kenar



a=Kare(4)
b=Dikdörtgen(3,2)
print(a.alan())
print(b.cevre())






