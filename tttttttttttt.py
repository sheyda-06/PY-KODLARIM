class BankaHesabi:
    def __init__(self, hesap_no, bakiye):
        self.__hesap_no = hesap_no   # Özelliği gizlemek için '__' kullanıyoruz
        self.__bakiye = bakiye

    def para_yatir(self, miktar):
        if miktar > 0:
            self.__bakiye += miktar
            print(f"{miktar} TL yatırıldı, yeni bakiye: {self.__bakiye} TL")

    def para_cek(self, miktar):
        if 0 < miktar <= self.__bakiye:
            self.__bakiye -= miktar
            print(f"{miktar} TL çekildi, kalan bakiye: {self.__bakiye} TL")
        else:
            print("Yetersiz bakiye")

    def bakiye_goster(self):
        return self.__bakiye

# Banka hesabı nesnesi oluşturma
hesap = BankaHesabi("123456", 500)
hesap.para_yatir(200)  # Çıktı: 200 TL yatırıldı, yeni bakiye: 700 TL
hesap.para_cek(100)    # Çıktı: 100 TL çekildi, kalan bakiye: 600 TL
print(hesap.bakiye_goster())  # Çıktı: 600
