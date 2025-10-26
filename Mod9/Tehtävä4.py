import random

from Classes.Car import Car

autot = []

for i in range(10) :
    randomSpeed = random.randint(100,200)
    newCar = Car("ABC-"+str(i+1),randomSpeed)
    autot.append(newCar)



for auto in autot:

    kokonaismatka = 0
    while kokonaismatka< 10000 :
        nopeusmuutos= random.randint(-10,15)
        auto.kiihdyta(nopeusmuutos)
        auto.kulje(1)
        kokonaismatka += auto.matka

        print(f"{auto.rekisteri} on kulkenut {kokonaismatka:0.2f}m" )





