vuodenAjat = ("kevät","kesä","syksy","talvi")

kuukausi = int(input("Syötä kuukauden numero: "))

if 6>kuukausi>2 :
    print(vuodenAjat[0])
elif 9>kuukausi>=6 :
    print(vuodenAjat[1])
elif 12>kuukausi>8 :
    print(vuodenAjat[2])

elif kuukausi<3 or kuukausi==12 :
     print(vuodenAjat[3])
