class Julkaisu :
    def __init__(self,nimi):
        self.nimi = nimi


    def tulosta_tiedot(self):

        print(f"{self.nimi}")
        return


class Kirja(Julkaisu):
        def __init__(self,nimi,kirjoittaja,sivumaara,):
            super().__init__(nimi)

            self.kirjoitta =kirjoittaja
            self.sivuMaara = sivumaara


        def tulosta_tiedot(self):
            super().tulosta_tiedot()
            print(f"{self.kirjoitta}:{self.sivuMaara} ")


class Lehti(Julkaisu):
      def __init__(self,nimi,paatoimittaja):
        
         super().__init__(nimi)
         self.paaToimittaja = paatoimittaja
      def tulosta_tiedot(self):
          super().tulosta_tiedot()
          print(f"{self.paaToimittaja}")