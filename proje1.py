class Kullanıcı:
    def __init__(self,kullanıcıad,email,şifre):
        self.kullanıcıad=kullanıcıad
        self.email=email
        self.şifre=şifre

    def profgörntüle(self,kişiara):
        if kişiara==self.kullanıcıad:
            print(f"{self.kullanıcıad}'ın profili görüntülenmiştir")
        else:
            print(f"{kişiara}'nın ppsi görüntülenemedi")

    def girisyap(self,girisyap):
        if girisyap==self.şifre:
            print("sifre dogru giriş yapılmıştır")
        else:
            print("yanlış giriş deneyimi")

    def çıkışyap(self):
        print("çıkış yapıldı...")



class kul1(Kullanıcı):
    def __init__(self,bio,takipedilenler):

        self.bio=bio
        self.takipedilenler=[]

    def takipet(self,takipet):
        self.takipedilenler.append(takipet)
        print(f"takip edilenler===={self.takipedilenler}")
    
    def begen(self,kişi):
        if kişi in self.takipedilenler :
            print(f"{kişi}nin gönderisi begenildi")
        else:
            print("kişi bulunamadıgı için begenilemedi")
    

    def takibibırak(self,bırak):
        if bırak in self.takipedilenler:
            self.takipedilenler.remove(bırak)
            print( f"{bırak} silindi yeni takipedilenler== {self.takipedilenler }")
        else:
            print("takip edilenlerde böyle bi isim bulunamadı")


    def biodegis(self,yeni):
        self.bio=yeni
        print(f"yeni bionuz:{self.bio}")

    def bilgiver(self):
        print(f"biosu=={self.bio} takipçilri={self.takipçiler} takip ettikleri={self.takipedilenler}")


class Paylaş(Kullanıcı):
    def __init__(self,kullanıcıad,email,şifre,postsayısı,storysayısı):
        super().__init__(kullanıcıad,email,şifre)
        self.postsayısı=0
        self.storysayısı=0



    def postat(self,miktar):
            self.postsayısı+=miktar
            print(f"{self.kullanıcıad} tarafından {miktar} kadar yeni post paylaşıldı. yeni post sayınız=={self.postsayısı}")


    def storyat(self,miktar):
        self.storysayısı+=miktar
        print(f"{self.kullanıcıad} tarafından {miktar} kadar yeni story paylaşıldı. yeni story sayınız=={self.storysayısı}")


    def bilgi(self):
        print(f"{self.kullanıcıad}'ın {self.postsayısı}kadar postu var{self.storysayısı}kadar storysi var")



    def yorum(self,yorum):
        print(f"{self.kullanıcıad} tarafından {yorum} yorumu yapıldı")



a=Paylaş("Ali", "ali@example.com", "sifre123", 0, 0)
a.postat(11)
a.postat(10)
a.yorum("başarılar dilerim")
a.storyat(20)
a.postat(9)
a.bilgi()



"""suheda=Kullanıcı("sheyda","shd@gmail.com",3883)
suheda.profgörntüle("sheyda1")
suheda.girisyap(383)
suheda.çıkışyap()"""


"""haydar=kul1("istanbul","anne","ögretmen")
haydar.takipet("baba")
haydar.takipet("abi")
haydar.takipet("abla")
haydar.takibibırak("abi")
haydar.begen("baba")
haydar.begen("anne")
haydar.takibibırak("baba")
haydar.biodegis("aslan ")
haydar.biodegis("basak")
haydar.bilgiver()"""











