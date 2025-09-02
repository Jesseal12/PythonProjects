luku = int(input("Anna kokonaisluku ja lopeta tyhjällä merkkijonolla : " ))
luvut = []
first = False

while(luku !=0):
      luvut.append(luku)
      luvut.sort()
      luku = int(input("Anna kokonaisluku ja lopeta 0:lla : "))

print(f"{luvut[-1]} {luvut[-2]} {luvut[-3]} {luvut[-4]} {luvut[-5]} ")

