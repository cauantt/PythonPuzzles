class Musico:


    @property
    def tocar(self):

        print("Tocando instrumento")




class Atleta:

   

    @property
    def correr(self):

        print("\nCorrendo na pista")


class MusicoAtleta(Musico, Atleta):

    def __init__(self):

        Musico.__init__(self)

        Atleta.__init__(self)

    @property
    def mostrarhabilidades(self):

        print("tocando instrumento e correndo")

musicoatleta = MusicoAtleta()


musicoatleta.correr

musicoatleta.tocar

musicoatleta.mostrarhabilidades

    
  


    