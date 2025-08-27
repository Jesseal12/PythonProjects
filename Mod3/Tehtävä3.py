sukupuoli = input("Anna sukupuolisi joko iso M tai Mies ja is N tai Nainen :  ")
hemoT = float(input("Anna hemoglobiinitasosi : "))
minHM =134
maxHM =195
minHN=117
maxHN=175
if sukupuoli =="M" or sukupuoli =="Mies" :
  if minHM < hemoT < maxHM :
      print("Teidän hemoglobiini tasot ovat normaalit")
  elif hemoT < minHM :
      print("teidän hemoglobiini  tasot ovat alhaiset")
  elif hemoT > maxHM :
      print("Teidän hemoglobiinitasot ovat liian korkeat")
  else:
       print("Oletteko edes elossa")


elif sukupuoli =="N" or sukupuoli =="Nainen" :
  if minHN <hemoT < maxHN :
      print("Teidän hemoglobiini tasot ovat normaalit")
  elif hemoT < minHN :
      print("teidän hemoglobiini  tasot ovat alhaiset")
  elif hemoT > maxHN :
      print("Teidän hemoglobiinitasot ovat liian korkeat")
  else:
       print("Oletteko edes elossa")
else:
     print("tuntematon sukupuoli input")






