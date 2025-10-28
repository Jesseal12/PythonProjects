class Julkaisu :
    def __init__(self,nimi):
        self.nimi = nimi


    def tulosta_tiedot(self):


        return


class Kirja(Julkaisu):
        def __init__(self,kirjoittaja,sivumaara):
            self.kirjoitta =kirjoittaja
            self.sivuMaara = sivumaara
            super().__init__(self.nimi)