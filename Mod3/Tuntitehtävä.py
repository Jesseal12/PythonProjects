
ikaMaara = float(input("Syötä ikäsi"))
if ikaMaara >=  18 :
   print("Olet täysi-ikäinen ole hyvä")
else:
    print("Et ole täysi-ikäinen. Sinut lähetetään Gulagiin")
    ikatarvittu = 18 - ikaMaara
    print(f" Jos olisit odottanut : {ikatarvittu} vuotta. Olisit säästänyt elämäsi")