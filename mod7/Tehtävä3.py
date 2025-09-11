lentoKentat = {"EFHK": "Helsinki-Vantaa"}
lentoKentat["AGAR"] = "Ulawa-Airport"
lentoKentat["AGEV"] = "Geva-Airport"

paalla = True
haku= False
lisays = False
while paalla == True :
    print(" Tervetuloa Käyttäjä!")
    aloitus = input("Jos haluatte hakea lentokenttä, laitakaa haku"
                    ".Jos haluatte lisätä laittakaa lisää tai lopettakaa ohjelma lopeta komenolla lopeta :  ")
    if aloitus == "haku":
          haku= True
          paalla= False
    elif aloitus =="lisää" :
        lisays = True
        paalla = False
    elif aloitus =="lopeta" :
        paalla=False
while haku :
    koodi = input("Syötä ICAO koodi tai lopeta ohjelma lopeta komenolla :")
    for i in lentoKentat :
            if i == koodi:
             print(f"Löytyi lentokenttä{lentoKentat[i]}")
            else:
                  print("Ei löytynyt hakemaasi lentokenttää")
    if koodi == "lopeta":
        print("Kiitos käytöstä")
        haku = False
while lisays :
       lisaaA = input("Syötä ICAO koodi tai lopeta ohjelma lopeta komenolla")
       lisaaB = input("Syötä Lentokentän nimen tai lopeta ohjelma lopeta komenolla")
       if lisaaA =="lopeta" or lisaaB == "lopeta":
          print("Kiitos käytöstä")
          lisays= False
       else:
        lentoKentat[lisaaA]=lisaaB
        print(f"Lentokenttä {lisaaA} {lisaaB} on lisätty ")
       print(lentoKentat)