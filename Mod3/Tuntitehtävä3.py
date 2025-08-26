matikkaArvosana = float(input(" Syötä Matikka arvosanasi"))
fysiikaArvosana = float(input("Syötä fysiikka arvosanasi"))
kemiaArvosana = float(input("Syötä kemia arvosanasi"))
mahdollinenPääsy = 0
if matikkaArvosana>=90 and fysiikaArvosana>= 90 or kemiaArvosana>= 95:
  print(" harkitaan stipendiä")
  # en osaa bool functiota joten teen oman boolin
  mahdollinenPääsy = 1
else :
    print("et saa stipendiä")
if mahdollinenPääsy==1 and matikkaArvosana>=50 and fysiikaArvosana >= 50 and kemiaArvosana>=50:
   print("Saat stipendin")

else :
      print("et saa stipendiä")
      