import math


def pizzaTime(sentit,euro):
    pintaAla = (sentit/2**2)*math.pi
    hinta = pintaAla / 100 * euro


    return hinta

keskiSyote = float(input("Syötä keskikokoisen pizzan halkaisija senttimetreinä: "))
keskiHinta = float(input("Anna keskikoko hintaluokan euroina per 100 senttiä :"))
isoSyote = float(input("Syötä isokokoisen pizzan halkaisija senttimetreinä :"))
isoHinta = float(input("Syötä iso koko hintaluokan euroina per 100 senttiä : "))
keskiPizza = pizzaTime(keskiSyote,keskiHinta)
isoPizza = pizzaTime(isoSyote,isoHinta)

if keskiPizza>isoPizza :
    print(f"Osta ison pizza. Saat {keskiPizza-isoPizza:0,2f} euroa edullisemman hinnan")
elif keskiPizza<isoPizza:
    print(f"Osta keskikokoisen pizzan. Saat {isoPizza-keskiPizza} euroa edullisemman hinnan")
else:
     print("Osta minkä pizzan haluat")
