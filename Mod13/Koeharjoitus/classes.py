



class Hoitola :
    def __init__(self,):
        self.Koirat = []


    def sisään(self,koira):
        self.Koirat.append(koira)


class Koira :
    koirat = 0
    def __init__(self, nimi, vuosi):
       Koira.koirat+=1
       self.nimi = nimi
       self.vuosi=vuosi
       self.koira = Koira.koirat


    def hauku(self,kerrat):

        return kerrat
class PieniKoira(Koira) :
    def __init__(self,nimi,vuosi,koko):
       # super().__init__(nimi,vuosi)
       Koira.__init__(self,nimi,vuosi)

    def hauku(self,kerrat):
        Koira.hauku(self,kerrat)
        super().hauku(kerrat)
