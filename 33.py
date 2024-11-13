class Arac:
    def __init__(self,hız):
        self.hız=hız



    def hızlan(self,miktar):
        self.hız+=miktar
        return self.hız
    

    def yavasla(self,miktar):
        self.hız-=miktar
        return self.hız
    

class Araba(Arac):
    def __init__(self,hız):
        super().__init__(hız)

    def hızkontrol(self):
        if self.hız >=120:
            print(f"hız çok yüksek")
        else:
           print("hız güvenli")
        
a=Araba(10 ) 
(a.hızkontrol())



    





