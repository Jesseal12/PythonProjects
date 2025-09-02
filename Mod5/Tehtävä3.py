numero = float(input(" Syötä numero tarkistakseen onko alkio: "))


if (numero>0 and numero %2 != 0 and numero %3 !=0 and numero % 5 != 0 and numero%7!=0):
    print( " Numero on alkio")
else:
    print("Numero ei ole alkio")