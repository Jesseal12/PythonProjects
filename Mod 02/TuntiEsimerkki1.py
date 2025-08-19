import math

ympyranSade = input("syötä ympyrän säde")
sivunPituus = input("Syötä neliön sivun pituus")

ympyraAla = math.pi* float(ympyranSade)**2
nelioAla = float(sivunPituus)**2
print(f"ympyrän pinta ala on {ympyraAla:.2f}")
print(f"Nelion pinta-ala on {nelioAla:.2f}")
