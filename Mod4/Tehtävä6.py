import random

N= random.randint(1,1000000)
n = 0
toisto = 0
while toisto!=N:
    xPiste = random.randint(-1,1)
    yPiste = random.randint(-1,1)
    toisto += 1
    if xPiste**2 + yPiste**2 < 1 :
        n +=1
likiMaara = 4*n/N

print(f"pi:n likimäärä on {likiMaara:0.2f} ")
#n/N≈π/4, π≈4n/N
