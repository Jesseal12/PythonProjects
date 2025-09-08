sumList = []
tempList = []
sum = 0
arvo = float(input(" Syötä kokonais tai desimaalilukuja jotka eivät ole nolla tai pienempi : "))
def isFull(list) :
    for luku in list :
      if luku % 1 ==0:
          sumList.append(luku)


    return


while arvo>0 :
    tempList.append(arvo)
    arvo = float(input(" Syötä kokonais tai desimaalilukuja jotka eivät ole nolla tai pienempi : "))
listaSum = isFull(tempList)
for t in sumList:
    sum += t
print(sumList)
print(f"Listan yhteen laskettu summa on {sum}")