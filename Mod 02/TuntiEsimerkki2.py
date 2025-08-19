banaaniMaara = input(" Syötä banaanien paino")
omenaMaara = input("Syötä omenoiden paino")
appelsiiniMaara = input("Syötä appelsiinien paino")

banaaniKiloHinta = 1.2

omenaKiloHinta = 3.15

appelsiiniKiloHinta = 4.05
banaaniHinta = banaaniKiloHinta*float(banaaniMaara)
omenaHinta = omenaKiloHinta* float(omenaMaara)
appelsiiniHinta =  appelsiiniKiloHinta*float(appelsiiniMaara)
summa = banaaniHinta+omenaHinta+appelsiiniHinta
print("Ostosten yhteenveto:")

print(f"banaanit :{banaaniHinta:0.2f}$ ")
print(f"Omenat : {omenaHinta:0.2f}$")
print(f"Appelsiinit :{ appelsiiniHinta:0.2f}$ ")
print (f"Yhteensä : {summa:0.2f}$")