class Termostato:

    def __init__(self,tempatual=20):

        self.tempatual = tempatual


    def aumentartemp(self,valor):

        self.tempatual += valor

        print(f"temperatura aumentada em {valor}, temperatura atual = {self.tempatual}")

    def diminuirtemp(self,valor):

        self.tempatual -= valor

        print(f"temperatura reduzida em {valor}, temperatura atual = {self.tempatual}")

    def configurartemp(self, novatemp):

        self.tempatual = novatemp 

        print(f"Temperatura ajustada para {self.tempatual}")
    
    def mostrartemp(self):

        print(f"Temperatura atual é de = {self.tempatual}")
termostato = Termostato()
termostato.diminuirtemp(10)

termostato.aumentartemp(5)

termostato.configurartemp(40)
termostato.aumentartemp(5)

termostato.mostrartemp()




    


