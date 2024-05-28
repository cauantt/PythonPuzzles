class Pet:

    def __init__(self, nome, idade, peso):
        self._nome = nome 
        self._idade = idade 
        self._peso = peso

    def set_nome(self, nome):
        self._nome = nome

    def set_idade(self, idade):
        self._idade = idade

    def set_peso(self, peso):
        self._peso = peso

    def get_nome(self):
        return self._nome

    def get_idade(self):
        return self._idade

    def get_peso(self):
        return self._peso
    
    def exibirinfo(self):
        print(f"Nome do pet: {self.get_nome()}")
        print(f"Idade do pet: {self.get_idade()}")
        print(f"Peso do pet: {self.get_peso()}")


def exibir_menu():
    print("1. Exibir informações do pet")
    print("2. Atualizar nome do pet")
    print("3. Atualizar idade do pet")
    print("4. Atualizar peso do pet")
    print("5. Sair")


def main():
    pet = Pet("Marquin", 5 ,  3.0)
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            pet.exibirinfo()
        elif opcao == "2":
            novo_nome = input("Novo nome do pet: ")
            pet.set_nome(novo_nome)
        elif opcao == "3":
            nova_idade = int(input("Nova idade do pet: "))
            pet.set_idade(nova_idade)
        elif opcao == "4":
            novo_peso = float(input("Novo peso do pet: "))
            pet.set_peso(novo_peso)
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
