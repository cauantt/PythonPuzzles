class Manipulador:

    def __init__(self):

        self.lista = []

    def  adicionar(self,valor):

        self.lista.append(valor)

    def mostrar(self):

        if len(self.lista) == 0:

            print("A lista está vazia")

        else:

            print(f"Lista: {self.lista}")

    def remover(self,valor):

        if valor not in self.lista:

            print("\nValor não encontrado")

        else:

            self.lista.remove(valor)

            print(f"O elemento {valor} foi removido")

    def maior(self):
        
        if len(self.lista) == 0:

            print("\nA lista está vazia")

        else:

            maior = 0

            for termo in self.lista:
                if maior < termo:
                    maior = termo

            print(f"\nO maior termo é: {maior}")


    def menor(self):

        if len(self.lista) == 0:

            print("\nA lista está vazia")

        else:

            menor = self.lista[0]

            for termo in self.lista:

                if menor > termo:
                    menor = termo

                print(f"\nO menor termo é: {menor}")

    def media(self):

        if len(self.lista) == 0:

            print("\nA lista está vazia")

        else:

            soma = 0

            for termo in self.lista:
                soma += termo

            print(f"\nA media dos numeros é: {soma/len(self.lista)}")

manipulador = Manipulador()

while True:
        
        print("-=" * 15)
        print("1. Adicionar elemento")
        print("2. Remover elemento")
        print("3. Encontrar maior elemento")
        print("4. Encontrar menor elemento")
        print("5. Calcular media")
        print("6. Mostrar lista")
        print("7. Sair")
    
        print("-=" * 15)

        opcaomenu = input("\nSelecione a opção: ")

        if opcaomenu == "1":

            try:
                valor = int(input("Qual número deseja adiconar:  "))
                manipulador.adicionar(valor)

            except ValueError:

                print("Entrada inválida, por favor insira um número inteiro")

        elif opcaomenu == "2":
            try:

                valor = int(input("Qual número deseja remover:  "))
                manipulador.remover(valor)

                

            except ValueError:

                print("Entrada inválida, por favor insira um número inteiro")


        elif opcaomenu == "3":
            
            manipulador.maior()

        elif opcaomenu == "4":
            
            manipulador.menor()

        elif opcaomenu == "5":

         
            manipulador.media()
        elif opcaomenu == "6":
            
            manipulador.mostrar()

        elif opcaomenu == "7":  

            break

        else:

            print("\nOpção invalida, tente novamente")
         


    
