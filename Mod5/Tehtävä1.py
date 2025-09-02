import random
tulos = 0
kuutiot = []
heittomäärä = random.randint(5,10)
print(f"heittomäärä on:{heittomäärä}")
for kuutio in range(heittomäärä) :
    kuutioHeitto = random.randint(1,6)
    kuutiot.append(kuutioHeitto)
    tulos += kuutioHeitto
print(kuutiot)
print(tulos)