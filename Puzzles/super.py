class Veiculo:


    def __init__(self,modelo):
        
        self.modelo = modelo

 
    def exibirinfo(self):

        print(f"modelo: {self.modelo}\n")


class Carro(Veiculo):

    def __init__(self, modelo,cor):
        Veiculo.__init__(self,modelo)

        self.cor = cor

    def exibirinfo(self):

        super().exibirinfo()

        print(f"\nCor: {self.cor}")


carro = Carro("Civic", "Preto")

carro.exibirinfo()