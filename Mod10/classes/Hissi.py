class Hissi :
    def __init__(self,alinKerros,ylinKerros):
        self.alinKerros= alinKerros
        self.ylinKerros = ylinKerros
        self.kerros = self.alinKerros


    def siirryKerrokseen(self,kerros):

        if kerros<self.alinKerros or kerros>self.ylinKerros:
            print("Kerrosta ei ole")
            return

        while self.kerros>kerros :
              self.kerrosAlas()

        while self.kerros<kerros:
            self.kerrosYlos()
        return
    def kerrosYlos(self):
        self.kerros += 1
        print(f"Olemme nyt kerrokessa : {self.kerros}")
        return
    def kerrosAlas(self):
        self.kerros -= 1
        print(f"Olemme nyt kerroksessa :{self.kerros}")
        return


