import random

N= float(input("Syötä pisteiden määrä"))
n = 0
toisto = 0
while toisto!=N:
    xPiste = random.uniform(-1,1)
    yPiste = random.uniform(-1,1)
    toisto += 1
    if xPiste**2 + yPiste**2 < 1 :
        n +=1
likiMaara = 4*n/N

print(f"pi:n likimäärä on {likiMaara:0.2f} ")
#n/N≈π/4, π≈4n/N
