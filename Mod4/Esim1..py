luku = int(input("Anna positiivisen kokonaisluvun"))
check = 0
while luku > 0 and check <=luku :
    if 0 % 2 == 0:
        print(check)
    check= check+1


else :
    print("Luku on virhellinen")