import random

from Mod9.Classes.Car import Car
from Mod9.Tehtävä4 import kokonaismatka


class Kilpailu :
    def __init__(self,nimi,metrit,autolista):
        self.nimi = nimi
        self.kilometriMäärä = metrit/1000
        self.autoLista = []

        for i in range(autolista):
            randomSpeed = random.randint(100,200)
            Car("ABC"+str(i+1),randomSpeed)


    def tunti_kuluu(self,tuntiMäärä):

        for auto in self.autoLista:

            kokonaismatka = 0
            while kokonaismatka < self.kilometriMäärä:
                nopeusmuutos = random.randint(-10, 15)
                auto.kiihdyta(nopeusmuutos)
                auto.kulje(tuntiMäärä)
                kokonaismatka += auto.matka/1000

                print(f"{auto.rekisteri} on kulkenut {kokonaismatka:0.2f}m")


    def tulosta_tilanne(self):
        for auto in self.autoLista :
            print(f"auto :{auto.rekisteri} on kulkenut {kokonaismatka:0.2f}km  ")


    def kilpailu_ohi(self):
        for auto in self.autoLista :
            if kokonaismatka>=self.kilometriMäärä :
                return True
            else:
                return False
        return