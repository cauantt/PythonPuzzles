class Casa:

    def __init__(self,_largura, _altura):

        self._altura = _altura 

        self._largura = _largura

    @property
    def Largura(self):

        return self._largura
    
    @Largura.setter
    def setlargura(self,valor):

        self._largura = valor


r = Casa(40,20)

print(r.Largura)

r.setlargura = 20

print(r.Largura)




