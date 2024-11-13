class Film:
    def __init__(self, isim, yönetmen, yıl, tür):
        self.isim = isim
        self.yönetmen = yönetmen
        self.yıl = yıl
        self.tür = tür

    def __str__(self):
        return f"İsim: {self.isim}, Yönetmen: {self.yönetmen}, Yıl: {self.yıl}, Tür: {self.tür}"


class Filmkatalog:
    def __init__(self):
        self.filmler = []

    def filmekle(self, film):
        self.filmler.append(film)

    def filmsil(self, isim):
        for film in self.filmler:
            if film.isim == isim:
                self.filmler.remove(film)
                return f"{isim} filmi silindi."
        return f"{isim} bulunamadı."

    def filmara(self, isim):
        for film in self.filmler:
            if film.isim == isim:
                return str(film)
        return f"{isim} isimli film bulunamadı."

    def tum_filmleri_goster(self):
        if not self.filmler:
            return "Katalogda film yok."
        return "\n".join([str(film) for film in self.filmler])


# Test kodu
katalog = Filmkatalog()
film1 = Film("Suheda'nın Günlükleri", "Suheda Yadogdu", 2044, "Aşk")
film2 = Film("Başka Bir Gün", "Ahmet Yılmaz", 2023, "Dram")

katalog.filmekle(film1)
katalog.filmekle(film2)

print(katalog.filmara("Suheda'nın Günlükleri"))  # Film bulunduğunda bilgileri yazdırır
print(katalog.filmara("Kayıp Film"))  # Film bulunamazsa mesaj verir

print(katalog.tum_filmleri_goster())  # Katalogdaki tüm filmleri gösterir
print(film1)
