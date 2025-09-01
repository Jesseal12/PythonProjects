
syottoArvo = float(input("Anna niin monta lukuarvoa kuin haluat ja lopeta 0:lla : "))

arvot = []
minArvo = 0
maxArvo = 0
while syottoArvo != 0 :

    if minArvo == 0 and maxArvo == 0 :
        minArvo=syottoArvo
        maxArvo=syottoArvo
        arvot.insert(0,minArvo)
        arvot.insert(1,maxArvo)
        syottoArvo = float(input("Anna lukuarvo ja lopeta 0:lla : "))
    elif syottoArvo<minArvo :
        minArvo =syottoArvo
        arvot.insert(0, minArvo)
        syottoArvo = float(input("Anna lukuarvo ja lopeta 0:lla : "))

    elif syottoArvo>maxArvo :
         maxArvo = syottoArvo
         arvot.insert(1, maxArvo)


         syottoArvo = float(input("Anna lukuarvo ja lopeta 0:lla : "))
   # bug se jatkuvasti printaa 0 molemille arvoille. Yritin korjata lisäämällä listaan
    #jos se johtuisi siitä et loopissa ei pysy muistissa
    print(f"Pienin arvo on : {arvot[0]:0.2f} ja suurin arvo on : {arvot[1]:0.2f}")
