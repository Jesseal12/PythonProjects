import math

alkukorkeus = float(input("anna esineen korkeus"))
pKiihtyvyys = 9.81

kokonaisaika = math.sqrt(2*alkukorkeus/pKiihtyvyys)
aika = 0
while aika<kokonaisaika :
    matka = 0.5*pKiihtyvyys*aika**2
    print(f"Pudottu matka : {alkukorkeus-matka:0.2f}")
    aika = aika + 1


print(f"kokonaisaika : {kokonaisaika:0.2f}s")