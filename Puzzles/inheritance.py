class Pessoa:

    def __init__(self,nome,idade):

        self.nome = nome

        self.idade = idade

    @property
    def exibirinfo(self):


        print(f"{self.nome} possui {self.idade} anos")


class Estudante(Pessoa):

    def __init__(self,nome,idade,matricula):

        Pessoa.__init__(self,nome,idade)

        self.matricula = matricula 

    @property
    def exibirestudante(self):


        print(f"Aluno: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Matricula: {self.matricula}")

class Professor(Pessoa):

    def __init__(self,nome,idade,materia):

        Pessoa.__init__(self,nome,idade)

        self.materia = materia 

    @property
    def exibirprof(self):


        print(f"Professora: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Materia {self.materia}")



pessoa = Pessoa("Maria", 24)

estudante = Estudante("João", 21, 12345)

professora = Professor("Tania", 42, "Calculo 1")


pessoa.exibirinfo

estudante.exibirestudante

professora.exibirprof
