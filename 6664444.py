class Arac:
    def __init__(self, marka, model, yakıttür):
        self.marka = marka
        self.model = model
        self.yakıttür = yakıttür

    def __str__(self):
        return f"Marka: {self.marka}, Model: {self.model}, Yakıt Türü: {self.yakıttür}"


class Otomobil(Arac):
    def __init__(self, marka, model, yakıttür, kapısayı):
        super().__init__(marka, model, yakıttür)
        self.kapısayı = kapısayı

    def fonk(self):
        print(f"{self.marka} markalı arabanın {self.kapısayı} kadar kapısı var")


# Nesneleri oluştur
a = Arac("BMW", 2025, "elektrik")
b = Otomobil("Mercedes", 2024, "dizel", 4)

# __str__ metodunu kullanarak nesneyi yazdır
print(a)  # a nesnesi için __str__ metodunu çağırır
print(b)  # b nesnesi için __str__ metodunu çağırır

b.fonk()
