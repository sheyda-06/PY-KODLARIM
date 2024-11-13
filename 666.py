class Hayvan:
    def __init__(self):
        pass



        
    def sescıkar(self,ses): 
            
            self.ses=ses
            return self.ses



class Kedi(Hayvan):
    def __init__(self):
        super().__init__()


class Köpek(Hayvan):
     

    def __init__(self):
          super().__init__()

a=Kedi()
b=Köpek()
print(a.sescıkar("miyav"))
print(b.sescıkar("havv"))
