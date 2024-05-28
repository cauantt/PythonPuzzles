# Classes e objetos 

class livro:
    def __init__(self, titulo, autor, ano ):

        self.titulo = titulo
         
        self.autor = autor

        self.ano = ano


def descrição(self):
    print(f"Livro {self.titulo} publicado por {self.autor} em {self.ano}")

  
meu_livro = livro("1984","George Orwell", "1949")

descrição(meu_livro)

        

    