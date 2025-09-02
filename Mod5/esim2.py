from unittest import expectedFailure

arvo = int(input("Anna Kokonaisluku"))


if arvo<1 :
    raise Exception("Luku on liian pieni")
else:

 for i in range(arvo+1):
    if i%2==0 :
         print(i)

