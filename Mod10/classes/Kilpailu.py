import random
from tabulate import tabulate




class Kilpailu :
    def __init__(self,nimi,kilometrit,autolista):
        self.nimi = nimi
        self.kilometriMäärä = kilometrit
        self.autoLista = []




    def tunti_kuluu(self,tuntiMäärä):

        for auto in self.autoLista:



                nopeusmuutos = random.randint(-10, 15)
                auto.kiihdyta(nopeusmuutos)
                auto.kulje(tuntiMäärä)





    def tulosta_tilanne(self):
        tulostettavat = []
        for auto in self.autoLista :
            tulostettavat.append([auto.rekisteri,auto.maxV,auto.nopeus,auto.matka])
            print(tabulate(tulostettavat))


    def kilpailu_ohi(self):
        for auto in self.autoLista :
            if auto.matka>=self.kilometriMäärä :
                return True

        return False