class Pessoa:
     
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota




class Estudante(Pessoa):

    def __init__(self, nome, idade, nota):

        Pessoa.__init__(self,nome,idade,nota)

      
    def mostrar(self):

        

        print(f"Nome do aluno:  {self.nome}")
        print(f"Idade do aluno:  {self.idade}")
        print(f"Nota do aluno:  {self.nota}")

            

    def mostrartodos(self):


                        

            print(f"Nome do aluno:  {self.nome}")
            print(f"Idade do aluno:  {self.idade}")
            print(f"Nota do aluno:  {self.nota}")

    def atualizarnota(self,valor):

        self.nota = valor

                
        


def adicionar():
    nome = input("\nNome do estudante:  ")
    idade = int(input("\nIdade do estudante:  "))
    nota = float(input("\nNota do estudante:  "))  

    estudante = Estudante(nome, idade, nota)
    lista.append(estudante)

lista = [] 

while True:

        print("")
        print("-=" * 15)
        print("1. Adicionar um novo estudante")
        print("2. Atualizar a nota de um estudante existente")
        print("3. Vizualizar informações de um estudante")
        print("4. Listar todos os estudantes")
        print("5. Sair")
        print("-=" * 15)

        opcaomenu = input("Digite a opção que deseja:  ")

        if opcaomenu == "1":

            adicionar()

    
        elif opcaomenu == "2":
            
            nome = input("\nQual estudante deseja atualizar a nota:  ")
            valor = float(input("\nDigite a nova nota:  "))

            for estudante in lista:

                if estudante.nome == nome:

                    estudante.atualizarnota(valor)

        elif opcaomenu == "3":

            nome = input("\nQual estudante deseja mostrar as informações:  ")

            for estudante in lista:

                if estudante.nome == nome:

                    estudante.mostrar()


        elif opcaomenu == "4":

            for estudante in lista:

                estudante.mostrartodos()


        elif opcaomenu == "5":

            break




        



