from Classes.Car import Car,Sahkoauto,Polttomoottori

Sahko = Sahkoauto("ABC-15",180,52.5)
Poltto = Polttomoottori("ACD-123",165,32.3)

Sahko.kulje(3)
Poltto.kulje(3)
print(f"{Sahko.matka } km")
print(f"{Poltto.matka} km")
#tehtäväanossa ei olla specifisoitu halutaanko akku ja bensan kuluvan joten en ole lisänyt niitä funktion ominaisuudeksi
