class Nodo:
    def __init__(self, info):
        self.info = info
        self.prox = None
class PilhaEncadeamento:
    def __init__(self):
        self.base = None
        self.topo = None
    def vazia(self):
        return self.topo == None or self.base == None
    def desempilha (self):
        if not self.vazia():
            self.topo = self.topo.prox
    def empilha(self, valor):
        novo = Nodo(valor)
        if not self.vazia():
            novo.prox = self.topo
        else:
            self.base = novo
        self.topo = novo
    def destroi(self):
        while not self.vazia():
            self.desempilha()
    def consultar(self):
        if not self.vazia():
            return self.topo.info