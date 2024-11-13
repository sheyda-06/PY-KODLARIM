class Hayvan:
    def __init__(self):
        pass
    
    def sescıkar(self, ses):
        self.ses = ses
        return self.ses

class Kedi(Hayvan):
    def __init__(self):
        super().__init__()

a = Kedi()
print(a.sescıkar("miyav"))  # Çıktı: miyav
