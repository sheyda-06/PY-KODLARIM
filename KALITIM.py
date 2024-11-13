class Hayvan:
    def __init__(self, ad, tur, yas, yasam_alani):
        self.ad = ad
        self.tur = tur
        self.yas = yas
        self.yasam_alani = yasam_alani

    def bilgileri_goster(self):
        print(f"Adı: {self.ad}")
        print(f"Türü: {self.tur}")
        print(f"Yaşı: {self.yas}")
        print(f"Yaşam Alanı: {self.yasam_alani}")


class Memeli(Hayvan):
    def __init__(self, ad, tur, yas, yasam_alani, dogum_yeri):
        super().__init__(ad, tur, yas, yasam_alani)
        self.dogum_yeri = dogum_yeri

    def bilgileri_goster(self):
        super().bilgileri_goster()
        print(f"Doğum Yeri: {self.dogum_yeri}")


class Kus(Hayvan):
    def __init__(self, ad, tur, yas, yasam_alani, ucma_hizi):
        super().__init__(ad, tur, yas, yasam_alani)
        self.ucma_hizi = ucma_hizi

    def bilgileri_goster(self):
        super().bilgileri_goster()
        print(f"Uçma Hızı: {self.ucma_hizi} km/h")


# Örnek kullanımlar
aslan = Memeli("Aslan", "Panthera leo", 5, "Orman", "Afrika")
kartal = Kus("Kartal", "Aquila chrysaetos", 4, "Dağlar", 160)

print("\nMemeli Hayvan Bilgileri:")
aslan.bilgileri_goster()

print("\nKuş Bilgileri:")
kartal.bilgileri_goster()

