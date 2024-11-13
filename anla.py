class Arac:
    def __init__(self,marka,model,yakıttür):
        self.marka=marka
        self.model=model
        self.yakıttür=yakıttür

    def __str__(self):
        return (f"markası={self.marka} modelii=={self.model} yakıttür={self.yakıttür}")



class Otomobil(Arac):
    def __init__(self,marka,model,yakıttür,kapısayı):
        super().__init__(marka,model,yakıttür)
        self.kapısayı=kapısayı

    def fonk(self):
        print(f"{self.marka} markalı arabanın {self.kapısayı} kadar kapısı var")


a=Arac("bmw",2025,"elektrik")
b=Otomobil("mercedec",2024,"dizel",11)

print(a)  # a nesnesi için __str__ metodunu çağırır
print(b)
b.fonk()


