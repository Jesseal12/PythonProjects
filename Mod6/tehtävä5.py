sumList = []
tempList = []

arvo = float(input(" Syötä kokonais tai desimaalilukuja jotka eivät ole nolla tai pienempi : "))
def isFull(list) :
    for luku in list :
      if  luku % 2==0 :
          sumList.append(luku)
          tempList.remove(luku)
    return


while arvo>0 :
      if arvo % 1 ==0 :
            tempList.append(arvo)


      arvo = float(input(" Syötä kokonais tai desimaalilukuja jotka eivät ole nolla tai pienempi : "))
listaSum = isFull(tempList)

print(sumList)
print(tempList)
