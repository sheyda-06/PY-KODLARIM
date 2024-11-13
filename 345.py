class Hayvan:
    def __init__(self,isim):
        self.isim=isim


    def sesçıkar(self):
        print(f"hayvan ses çıkarıyor")

class Köpek(Hayvan):
 
    def sescıkar(self):
        print(f"{self.isim}  ses çıkarıyor")


class Kedi(Hayvan):
    def sescıkar(self):
        print(f"{self.isim}miyavlıyor")

a=Köpek("KARABAS")
a.sescıkar()



