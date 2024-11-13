class Film:
    def __init__(self,isim,yönetmen,yıl,tür):
        self.isim=isim
        self.yönetmen=yönetmen
        self.yıl=yıl
        self.tür=tür

    def __str__(self):
        return(f"ismi={self.isim} yönetmen=={self.yönetmen} yılı=={self.yıl} tür=={ self.tür}")
    
class Filmkatalog:
    def __init__(self):
        self.filmler=[]


    def filmekle(self,ekle):
        self.filmler.append(ekle)
        return self.filmler
    

    def filmsil(self,sil):
        if sil in self.filmler:
            self.filmler.remove(sil)
            return self.filmler
        

    def filmara(self,ara):
        if ara==self.isim:
            print(f"{ara}  filminın bilgileri ismi={self.isim} yönetmen=={self.yönetmen} yılı=={self.yıl} tür=={ self.tür}")

a=Filmkatalog()
b=Film("suhedsnın günlük","suhedayadogddu",2044,"ask")
a.filmara("suhedsnın günlük")



               
