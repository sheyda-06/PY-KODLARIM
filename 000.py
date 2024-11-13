class Bank:
    def __init__(self):
        
        self.bakiye=int(input("bakiyenizi giriniz:"))


    def paracek(self,miktar):
        if miktar<self.bakiye:
            self.bakiye-=miktar
            return self.bakiye
        else:
            print("yetersiz bakiyee")

    def parayatır(self,miktar):
        self.bakiye+=miktar
        return self.bakiye

    def göster(self):
        return self.bakiye

    def havaleet(self,kişi,miktar):
        if miktar<self.bakiye:
            self.bakiye-=miktar

            print(kişi,"kişisine",miktar,"tl gönderildi")
            print("havaleden sonrakiyeni bakiyeniz",self.bakiye)
        else:
            print("yetersiz bakiye")

c1=Bank()
print(c1.havaleet("mustafa",100))

