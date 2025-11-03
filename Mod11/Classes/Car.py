class Car:
    def __init__(self, rekisteri, maxV):
        self.rekisteri = rekisteri
        self.maxV = maxV
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, arvo):
        muutos = self.nopeus + arvo

        if muutos > self.maxV:
            self.nopeus = self.maxV

        elif muutos < 0:
            self.nopeus = 0


        else:
            self.nopeus = muutos

        return

    def kulje(self, aika):
        self.matka += self.maxV * aika

        return

class Sahkoauto(Car):
    def __init__(self,rekisteri,maxV,akkukapasiteetti):
        super().__init__(rekisteri,maxV)
        self.akkuKapasiteetti=akkukapasiteetti
        self.matka=0
        
    def kulje(self,aika):
        super().kulje(aika)

class Polttomoottori(Car):
    def __init__(self,rekisteri,maxV,bensatankki):
        super().__init__(rekisteri,maxV)
        self.bensaTankki=bensatankki
        self.matka= 0
    
    def kulje(self,aika):
        super().kulje(aika)