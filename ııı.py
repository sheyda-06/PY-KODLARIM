# Ana sınıf: Kullanıcı
class Kullanıcı:
    def __init__(self, kullanıcıad, email, şifre):
        self.kullanıcıad = kullanıcıad
        self.email = email
        self.şifre = şifre

    def profgörntüle(self, kişiara):
        if kişiara == self.kullanıcıad:
            print("Profil görüntülenmiştir")
        else:
            print("Görüntülenemedi")

    def girisyap(self, girilen_sifre):
        if girilen_sifre == self.şifre:
            print("Giriş yapılmıştır")
        else:
            print("Yanlış giriş deneyimi")

    def çıkışyap(self):
        print("Çıkış yapıldı...")


# Alt sınıf: kul1
class kul1(Kullanıcı):
    def __init__(self, kullanıcıad, email, şifre, bio):
        # Ana sınıfın __init__ fonksiyonunu çağırıyoruz
        super().__init__(kullanıcıad, email, şifre)
        self.bio = bio
        self.takipçiler = []  # Başlangıçta boş liste
        self.takipedilenler = []  # Başlangıçta boş liste

    def takipet(self, takipet):
        self.takipedilenler.append(takipet)
        return self.takipedilenler

    def begen(self, kişi):
        if kişi in self.takipedilenler or kişi in self.takipçiler:
            print(f"{kişi}nin gönderisi beğenildi")
        else:
            print("Kişi bulunamadığı için beğenilemedi")

    def takibibırak(self, bırak):
        if bırak in self.takipedilenler:
            self.takipedilenler.remove(bırak)
            print(f"{bırak} takipten çıkarıldı.")
        else:
            print("Takip edilenlerde böyle bir isim bulunamadı")

    def biodegis(self, yeni):
        self.bio = yeni
        print(f"Yeni bionuz: {self.bio}")

    def bilgiver(self):
        print(f"Bio: {self.bio}, Takipçiler: {self.takipçiler}, Takip Ettikleri: {self.takipedilenler}")


# Kullanıcı nesneleri oluşturalım
a = kul1("shyda", "shdayy@example.com", 3883, "pc müh")
b = kul1("basak", "basak@example.com", 1234, "tıp öğrencisi")

# Takip etme işlemleri
print(a.takipet("irem"))  # Çıktı: ['irem']
print(b.takipet("yagmur"))  # Çıktı: ['yagmur']

# Takip bırakma işlemi
print(a.takibibırak("irem"))  # Çıktı: irem takipten çıkarıldı.

# Beğenme işlemi
print(a.begen("yagmur"))  # Çıktı: Kişi bulunamadığı için beğenilemedi

# Bio değiştirme
print(b.biodegis("ikiz"))  # Çıktı: Yeni bionuz: ikiz

# Bilgi görüntüleme
print(a.bilgiver())  # Çıktı: Bio: pc müh, Takipçiler: [], Takip Ettikleri: []
