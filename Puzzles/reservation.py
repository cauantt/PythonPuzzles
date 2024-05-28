class Evento:

    def __init__(self,lugares=10):

        self.lugares = lugares


    def reserva(self,valor):


        if self.lugares == 0:

            print("\nTodos lugares já estão reservados!")
        
        else:

            

            for i in range (valor):

                print("\nLugar reservado com sucesso!!!")

                self.lugares -= 1

    def cancelar(self,valor):

        if self.lugares == 10:

            print("\nNão possue reservas para serem canceladas")

        else:


            for i in range (valor):

                print("\nReserva cancelada com sucesso!!!")

                self.lugares += 1



    def disponivel(self):

        print(f"\nLugares disponiveis: {self.lugares}")

evento = Evento()
    

while True:

        print("")
        print("-=" * 15)
        print("1. Reservar")
        print("2. Cancelar")
        print("3. Lugares disponivel")
        print("4. Sair")
        print("-=" * 15)

        opcaomenu = input("Digite a opção que deseja:  ")

        if opcaomenu == "1":

            valor = int(input("Digite quantos quer reservar:  "))

            evento.reserva(valor)



        elif opcaomenu == "2":
            
            valor = int(input("Digite quantas reservas quer cancelar:  "))

            evento.cancelar(valor)



        elif opcaomenu == "3": 

            evento.disponivel()

        
        elif opcaomenu == "4":

            break

        else:

            print("Opção invalida, tente novamente!")

