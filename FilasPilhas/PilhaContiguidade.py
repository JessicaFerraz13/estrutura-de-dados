class PilhaContiguidade:
    def __init__(self, max):
        self.lim = max - 1
        self.vetor = [None] * (self.lim + 1)
        self.base = 0
        self.topo = -1
    def vazia(self):
        return self.topo == -1
    def empilha(self,dado):
        if self.topo < self.lim:
            self.topo = self.topo + 1
            self.vetor[self.topo] = dado
    def consultar(self):
        if not self.vazia():
            return self.vetor[self.topo]
    def destroi(self):
        self.topo = -1
    def desempilha(self):
        if not self.vazia():
            self.topo = self.topo - 1