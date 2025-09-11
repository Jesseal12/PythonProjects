
nimet = {"Jesse"}


nimiSyotto = input("Anna Henkilön nimen ja lopeta tyhjällä merkkijonolla :")


while nimiSyotto != "":
    if nimiSyotto in nimet:
        print("Nimi on jo joukossa")

    else:
       print("Uusi nimi")
       nimet.add(nimiSyotto)
    nimiSyotto = input("Anna Henkilön nimen ja lopeta tyhjällä merkkijonolla :")
print(nimet)    