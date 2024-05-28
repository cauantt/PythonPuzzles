from time import sleep



class Pessoa:

    def __init__(self,nome):

        self.nome = nome
        self.acordado = True
        self.comendo = False
        self.dirigindo = False


    def acordar(self):

        if self.acordado:
            
            print(f"\n{self.nome} já esta acordado")
        
        elif self.dirigindo:
 
            print(f"\n{self.nome} está dirigindo")

        elif self.comendo:

            print(f"\n{self.nome} está comendo")

        else: 
            print(f"\n{self.nome} está acordando...")
            sleep(1.0)
            print(f"{self.nome} acordou!")
            
            self.acordado = True

    def dormir(self):

        if not self.acordado:
            
            print(f"\n{self.nome} já esta dormindo")
        
        elif self.dirigindo:
 
            print(f"\n{self.nome} morreu!")

            

        elif self.comendo:

            print(f"\n{self.nome} não pode dormir enquanto está comendo")

        else: 
            print(f"\n{self.nome} está indo dormir....")
            sleep(1.0)

            print(f"\n {self.nome} dormiu!!")
            
            self.acordado = False

    
            
            
    
    def comer(self,comida):

        
        if self.dirigindo:

            print(f"\n{self.nome} não pode comer enquanto dirige")
        
        elif not self.acordado:

            print(f"\n{self.nome} não pode comer enquanto dorme")

        elif self.comendo:

            print(f"\n{self.nome} ja está comendo")

        else:
            print(f"\n{self.nome} esta preparando sua refeição....")
            sleep(1.0)
            print(f"\n{self.nome} começou a comer {comida}")
            self.comendo = True

    def parardecomer(self):

        if not self.comendo:

            print(f"\n{self.nome} não está comendo")
            
            
        
        elif self.dirigindo:

            print(f"\n{self.nome} está dirigindo")
        
        elif not self.acordado:

            print(f"\n{self.nome} está dormindo")

        else:

            print(f"\n{self.nome} acabou de comer!")
            
            self.comendo = False
        
    def dirigir (self,destino):

        if self.comendo:

            print(f"\n{self.nome} não pode dirigir enquanto come")
            
            
        
        elif not self.acordado:

            print(f"\n{self.nome} morreu")
            
        
        elif self.dirigindo:

            print(f"\n{self.nome} já esta dirigindo")

        else:

            print(f"\n{self.nome} está entrando no carro...")
            sleep(1.0)
            print(f"\n{self.nome} começou a dirigir para: {destino}")

            
            self.dirigindo = True

    def parardedirigir (self):

        if self.comendo:

            print(f"\n{self.nome} está comendo")
            
            
        
        elif not self.acordado:

            print(f"\n{self.nome} está dormindo")
        
        elif not self.dirigindo:

            print(f"\n{self.nome} não está dirigindo")

        else:

            print(f"\n{self.nome} está estacionando o carro...")
            sleep(1.0)
            print(f"\n{self.nome} parou de dirigir!")

            
            self.dirigindo = False


       

pessoa = Pessoa("João")
        

while True: 

    print("")
    print("-=" * 15)
    print("1. Comer")
    print("2. Parar de comer")
    print("3. Dormir")
    print("4. Acordar")
    print("5. Dirigir")
    print("6. Parar de dirigir")
    print("7. Sair")
    print("-=" * 15)

    menu = input("\nSelecione a opção:  ")

    if menu == "1":
        comida = input("\nO que João vai comer?")
        pessoa.comer(comida)
        

    elif  menu == "2":

        pessoa.parardecomer()

    elif menu == "3":

        pessoa.dormir()
        
    elif menu == "4":

        pessoa.acordar()

    elif menu == "5":
        destino = input("\nPra aonde João vai?  ")
        pessoa.dirigir(destino)

    elif menu == "6":

        pessoa.parardedirigir()
    
    elif menu == "7":

        break


    else:

        print("Opção invalida, tente novamente")

