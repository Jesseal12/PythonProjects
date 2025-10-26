from .Hissi import Hissi
class Talo :
    def __init__(self,alinKerros,YlinKerros,hissit):
        self.alinKerros = alinKerros
        self.YlinKerros= YlinKerros
        self.hissitLkm = []
        for i in range(hissit) :
            self.hissitLkm.append(Hissi(self.alinKerros,self.YlinKerros))

    def ajaHissia(self,hissinNumero,kohdeKerros):
         print(f"ajat hisillä {hissinNumero}")
         self.hissitLkm[hissinNumero-1].siirryKerrokseen(kohdeKerros)

    def paloHalytys(self):
        print("Nyt on tulipalo 3 2 1 Let's jam")
        for hissi in self.hissitLkm :
            hissi.siirryKerrokseen(self.alinKerros)
        print(f"Kaikki hissit ovat {self.alinKerros} keroksessa")