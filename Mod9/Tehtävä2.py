from Classes.Car import Car


auto = Car("ABD-124",140)
auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)
print( f"Nopeus on : {auto.nopeus}")
auto.kiihdyta(-200)
print("Jarrutetaan")
print(f"Nopeus on nyt {auto.nopeus}")