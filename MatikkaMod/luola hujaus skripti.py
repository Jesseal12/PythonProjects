import random



luolassa = [3,5,9,11]


def laskeKombinaatiot() :

    while len(luolassa)>2:
         timeSpent=0
         randomValue1 = random.randint(0, len(luolassa))
         randomValue2 = random.randint(0,len(luolassa))
         if randomValue1 !=randomValue2:
            coinflip = random.randint(0,1)
            firstValue =luolassa[randomValue1]
            secondValue = luolassa[randomValue2]
         if coinflip==1 :
            timeSpent+=firstValue+secondValue
            print(f"{firstValue} ja {secondValue} lähtevät ja {firstValue} poistuu")
            luolassa.remove(firstValue)

         else:
           timeSpent+=secondValue+firstValue
           print(f"{firstValue} ja {secondValue} lähtevät ja {secondValue} poistuu")
           luolassa.remove(secondValue)


    return timeSpent



laskeKombinaatiot()
while laskeKombinaatiot()>=30:
    luolassa =[3,5,9,11]
    laskeKombinaatiot()



