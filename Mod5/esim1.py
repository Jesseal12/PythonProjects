
arvoSyotto = float(input("Syötä numero"))

arvot = []

while arvoSyotto>-1 :

          arvot.append(arvoSyotto)
          arvot.sort()
          arvoSyotto = float(input("Syötä numero"))
print(arvot)

for i in arvot:
     if i== 10 :
         print("Löytyi 10")

