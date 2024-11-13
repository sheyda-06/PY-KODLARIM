class Human:
    def __init__(self,adı,soyadı,statu,yas):
        self.adı=adı
        self.soyadı=soyadı
        self.statu=statu
        self.yas=yas


    def bilgi(self):
        print(f"adı={self.adı} soyadı={self.soyadı}")


class Engineer(Human):
    def __init__(self,adı,soyadı,statu,yas):
        super().__init__(adı,soyadı,statu,yas)


eng=Engineer("suheda","ayd","engineer", 25)
eng.bilgi()


