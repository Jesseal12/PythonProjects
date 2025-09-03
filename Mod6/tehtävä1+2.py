import random

tahko = int(input("Syötä suurin tahko luku:"))
def noppaHeitto(noppaTahko):
          noppa = random.randint(1,noppaTahko)
          return noppa
noppaArvo=0
heitot =0
while(noppaArvo!=tahko):

      noppaArvo= noppaHeitto(tahko)
      heitot += 1
print(f"Meni {heitot:0.2f} heittoa kunnes saatin nopan arvoksi {noppaArvo:0.2f}")