import random

nimiList = ["jesse","Saku","Tom"]
sukuList = ["Aaltonen","Reponen","Bloomqvist"]
kombinaatiot = {}

#löydä kaikki mahdollisset kombinaatiot nimi ja sukunimilistasta
def nimiKombinaatiot(nimet,sukunimet) :
    arvo1 =  random.randint(nimet[0],nimet[-1])
    arvo2 = random.randint(sukunimet[0],sukunimet[-1])


    return arvo1,arvo2

