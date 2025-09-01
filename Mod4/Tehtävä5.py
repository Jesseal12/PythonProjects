
oikeaKayttaja = "python"
oikeaSalis = "rules"
nimiSyotto = input("Syötä käyttäjä nimesi : ")
salisSyotto = input("Syötä salasana : ")
sallitutYritykset = 5
yritys = 0
while nimiSyotto != oikeaKayttaja or salisSyotto != oikeaSalis :
     if yritys !=sallitutYritykset:
        nimiSyotto = input("Syötä käyttäjä nimesi : ")
        salisSyotto = input("Syötä salasana : ")
        yritys += 1
     else:
          print("Olette väärä henkilö. Poliisi on tulossa pidättämään teidät")
          break

