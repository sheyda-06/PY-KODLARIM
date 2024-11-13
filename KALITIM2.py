class Calisan:
    def __init__(self, ad, soyad, tc_no, departman):
        self.ad = ad
        self.soyad = soyad
        self.tc_no = tc_no
        self.departman = departman




    def bilgileri_goster(self):
        print(f"Adı: {self.ad}")
        print(f"Soyadı: {self.soyad}")
        print(f"T.C. No: {self.tc_no}")
        print(f"Departman: {self.departman}")



class Yönetici(Calisan):
    def __init__(self,ad, soyad, tc_no, departman,yonetilen_departman):
        super().__init__(ad, soyad, tc_no, departman)
        self.yonetilen_departman=yonetilen_departman



    def bilgileri_goster(self):
        super().bilgileri_goster()
        print(f"Yönetilen Departman: {self.yonetilen_departman}")


class İsci(Calisan):

    def __init__(self,ad, soyad, tc_no, departman,calisma_saati):
        super().__init__(ad, soyad, tc_no, departman)

        self.calisma_saati=calisma_saati



    def bilgigoster(self):
        super().bilgileri_goster()
        print(f"Haftalık Çalışma Saati: {self.calisma_saati}")



yonetici = Yönetici("Ahmet", "Kara", "12345678901", "İnsan Kaynakları", "Satın Alma")
isci = İsci("Mehmet", "Çelik", "10987654321", "Üretim", 45)




