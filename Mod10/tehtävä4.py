from classes.Kilpailu import Kilpailu
import random
from Mod9.Classes.Car import Car
uusiKilpailu =Kilpailu(f"Suuri romuralli",8000,10)
for i in range(1,10):
    randomSpeed = random.randint(100, 200)
    uusiAuto=Car("ABC" + str(i + 1), randomSpeed)
    uusiKilpailu.autoLista.append(uusiAuto)
print(f"Kilpailu {uusiKilpailu.nimi} on alkanut!")

print(uusiKilpailu.autoLista)
tunti= 0
while not uusiKilpailu.kilpailu_ohi():

    uusiKilpailu.tunti_kuluu(1)

    tunti +=1
    if  tunti % 10 == 0:
        uusiKilpailu.tulosta_tilanne()