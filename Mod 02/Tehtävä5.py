leiviskat = float(input("anna leiviskät"))
naulat = float(input("anna naulat"))
luodit = float(input("anna luodit"))
leiviLuoti= leiviskat*20*32
naulatLuoti = naulat*32
massa= (leiviLuoti+naulatLuoti+luodit)*13.3
kilot = massa//1000
grammat = massa%1000
print(f"{kilot}kg {grammat:0.2f} g")