
energiaKulut = float(input(" Kuinka paljon sähköä kulutat?"))
if energiaKulut<=50 and energiaKulut >0 :
    hinta = energiaKulut * 0.10

    print(" Maksa 10 senttiä tunissa pummi")


elif energiaKulut <= 200 :
     hintaA = 50*0.10
     yli50 = energiaKulut-50
     hintaB = yli50*0.08
     hinta =hintaA + hintaB
elif energiaKulut> 200 :
    hintaA = 50*0.10
    hintaB = 150*0.08
    yli200 = energiaKulut-200

    hintaC = yli200*0.06
    hinta = hintaA + hintaB + hintaC
else:

    print(" Painu siitä rotta. Puhun pelkästään asiakkaille")

print(f"Joudut maksamaan {hinta} :euroa")
