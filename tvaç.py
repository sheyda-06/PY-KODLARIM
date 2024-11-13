class Television:
    def __init__(self):
        self.ison=True
        self.channel=1
        self.volume=5

    def turnon(self):
        if not self.ison:
                self.ison=True
                print("tv acıldı")

        else:
                print("zaten acık")

    def turnoff(self):
        if self.ison:
                self.ison=False
                print("tv kapandı")

        else:
              print("zaten kapalı")

    def changechannel(self,channel):
          if 1<=channel<=100:
                self.channel=channel
                print("şu anda",self.channel,"kanalındayız")
          else:
                print("böyle bir kanal mevcut degil")

    def volumeincrease(self):
          if self.ison==True:
            self.volume+=1
            return self.volume
    
    def volumedecrease(self):
          if self.ison==True:
                self.volume-=1
                return self.volume
          



a1=Television()
a1.turnon()
print(a1.volumedecrease())
print(a1.volumedecrease())
print(a1.changechannel(28))