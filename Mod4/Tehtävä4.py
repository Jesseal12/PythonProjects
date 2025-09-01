import random

anettuarvo = random.randint(1,10)
peliPaalla = True
arvausta = 0
while peliPaalla == True:

    arpominen = random.randint(1,10)
    if arpominen == anettuarvo :
        print(f"Oikea arvo, Meni : {arvausta:0.2f} arvausta arpomiseen ")
        peliPaalla = False
    elif anettuarvo>arpominen :
          print("Arvo on liian pieni")
          arvausta+=1
    elif anettuarvo<arpominen:
        print("Arvo on liian Iso")
        arvausta+=1