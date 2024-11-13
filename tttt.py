class Kitap:
    def __init__(self, adı, yazar, ISBN, yıl, durum="mevcut"):
        self.adı = adı
        self.yazar = yazar
        self.ISBN = ISBN
        self.yıl = yıl
        self.durum = durum  # Buradaki durum parametresi, varsayılan olarak "mevcut" olmalı

    def __str__(self):
        return (f"Adı: {self.adı}, Yazar: {self.yazar}, ISBN: {self.ISBN}, "
                f"Yıl: {self.yıl}, Durum: {self.durum}")


class Üye:
    def __init__(self, adı, numarası, eposta, tarihi):
        self.adı = adı
        self.numarası = numarası
        self.eposta = eposta
        self.tarihi = tarihi

    def __str__(self):
        return (f"Adı: {self.adı}, Numarası: {self.numarası}, Epostası: {self.eposta}, "
                f"Tarihi: {self.tarihi}")


class Kütüphane:
    def __init__(self):
        self.kitaplar = []
        self.üyeler = []
        self.saklalist = []

    def ekle(self, yeni):
        self.kitaplar.append(yeni)
        return self.kitaplar
    
    

    def tüm_kitapları_göster(self):
        if not self.kitaplar:
            print("Kütüphanede hiç kitap yok.")
        else:
            for kitap in self.kitaplar:
                print(kitap)  # Her bir kitabı yazdır

    

    def ödünçal(self, sil):
        for i in self.kitaplar:
            if i == sil:
                self.kitaplar.remove(sil)
                self.saklalist.append(sil)
                return f"{sil.adı} kitabı ödünç alındı."  # Mesaj döndürüyoruz
        return "Listelerde bu kitap olmadığından silinmedi."  # Mesaj döndürüyoruz
    
    def sakla(self):
        if self.saklalist:
            for i in self.saklalist:
                print(i)
        else:
            print("boş liste")

    def üyeekle(self, yeni):
        self.üyeler.append(yeni)
        return self.üyeler

    def durumbilgi(self, kitap_ismi):
        for i in self.kitaplar:
            if i.adı == kitap_ismi:
                return i.durum  # Kitabın durumunu döndür
        return "Kitap bulunamadı."


# Test kodu
kütüphane = Kütüphane()
kitap1 = Kitap("Suheda'nın Günlükleri", "Suheda Yadogdu", "123456", 2044)
kitap2 = Kitap("Başka Bir Gün", "Ahmet Yılmaz", "654321", 2023)

kütüphane.ekle(kitap1)
kütüphane.ekle(kitap2)

print(kütüphane.durumbilgi("Suheda'nın Günlükleri"))  # "mevcut" döner
print(kütüphane.ödünçal(kitap1))  # "Suheda'nın Günlükleri kitabı ödünç alındı."
print(kütüphane.durumbilgi("Suheda'nın Günlükleri"))  # "mevcut" döner
print(kütüphane.sakla())