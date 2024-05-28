class Formatadordefrase:

    def __init__(self, frase):
        self.frase = frase

    def maiuscula(self):
        self.frase = self.frase.upper()
        print(f"\nFrase formatada: {self.frase}")

    def minuscula(self):
        self.frase = self.frase.lower()
        print(f"\nFrase formatada: {self.frase}")

    def capitalizar(self):
        self.frase = self.frase.capitalize()
        print(f"\nFrase capítalizada: {self.frase}")

    def titulo(self):
        self.frase = self.frase.title()
        print(f"\nFrase capítalizada: {self.frase}")
    
    def contar_vogais(self):
        vogais = "aeiouAEIOU"
        resultado = 0
        for char in self.frase:
            if char in vogais:
                resultado += 1
        print(f"\nTotal de vogais: {resultado}")
    
    def contar_consoantes(self):
        consoantes = "bcdfghjklmnpqrstvxywzBCDFGHJKLMNPQRSTVXYWZ"
        resultado = 0
        for char in self.frase:
            if char in consoantes:
                resultado += 1
        print(f"\nTotal de consoantes: {resultado}")
            
    def contar_letra_a(self):
        a = "aA"
        resultado = 0
        for char in self.frase:
            if char in a:
                resultado += 1
        print(f"\nTotal de letras A: {resultado}")

    def pesquisar_palavra(self):

        palavra = input("\nDigite a palavra que deseja pesquisar:  ")
        cont = 0
        for i in self.frase.split():
            if i == palavra :
                cont += 1
        print(f"\nA palavra {palavra} aparaceu {cont} vezes")

    def mostrar_frase(self):
        print(f"\nA frase atual é: {self.frase}")                


        

def menu():
    frase = str(input("Digite a frase: "))
    formatador = Formatadordefrase(frase)

    while True:
        
        print("-=" * 15)
        print("1. Converter para maiúsculas")
        print("2. Converter para minúsculas")
        print("3. Capitalizar a primeira letra da frase")
        print("4. Converter para o formato título")
        print("5. Contar vogais")
        print("6. Contar consoante")
        print("7. Contar letra A")
        print("8. Pesquisar palavra")
        print("9. Mostrar frase atual")
        print("10. Sair")
        print("-=" * 15)

        opcaomenu = input("\nSelecione a opção: ")

        if opcaomenu == "1":
            formatador.maiuscula()
        elif opcaomenu == "2":
            formatador.minuscula()
        elif opcaomenu == "3":
            formatador.capitalizar()
        elif opcaomenu == "4":
            formatador.titulo()
        elif opcaomenu == "5":
            formatador.contar_vogais()
        elif opcaomenu == "6":
            formatador.contar_consoantes()
        elif opcaomenu == "7":
            formatador.contar_letra_a()
        elif opcaomenu == "8":
            formatador.pesquisar_palavra()
        elif opcaomenu == "9":
            formatador.mostrar_frase()
        elif opcaomenu == "10":
            break

if __name__ == "__main__":
    menu()
