import numpy  as np
yksiA = 2,493
yksiB = 0,911
kaksiA = 137.7
kaksiB =62,3

np.radians(kaksiA)
np.radians(kaksiB)

print(np.degrees(yksiA))
print(np.degrees(yksiB))
print(np.radians(kaksiA))
print(np.radians(kaksiB))

taulukkoLista = [30,45,60,90,120,135,150,180,270,360]


for i in taulukkoLista :
    print(np.radians(i))

a = 1.6
b = 2.3
hypotenuusa = np.hypot(a,b)
print(hypotenuusa)