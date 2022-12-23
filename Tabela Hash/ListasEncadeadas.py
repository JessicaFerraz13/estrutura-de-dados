class Nodo:
    def __init__(self, chave, info):
        self.info = info
        self.chave = chave
        self.prox = None
class ListaEncad:
    def __init__(self):
        self.inicio = None
    def vazia(self):
        return self.inicio == None
    def exclui(self, posicao):
        if (not self.vazia() and posicao > 0):
            if posicao == 1:
                self.inicio = self.inicio.prox
            else:
                i=1
                aux = self.inicio
                ant = None
                while (i< posicao and aux != None):
                    ant = aux
                    aux = aux.prox
                    i = i +1
                if aux != None:
                    ant.prox = aux.prox
    def insere(self, posicao, valor):
        if posicao > 0:
            novo = Nodo(valor)
            if posicao == 1:
                novo.prox = self.inicio
                self.inicio = novo
            else:
                aux = self.inicio
                i = 1
                while (i < posicao - 1 and aux != None):
                    aux = aux.prox
                    i = i + 1
                if aux != None:
                    novo.prox = aux.prox
                    aux.prox = novo
    def posicao(self, valor):
        aux = self.inicio
        i = 1
        while aux != None:
            if aux.info == valor:
                return i
            aux = aux.prox
            i = i + 1
        return 0
    def valor(self, posicao):
        if posicao > 0:
            aux = self.inicio
            i = 1
            while (i < posicao and aux != None):
                aux = aux.prox
                i = i + 1
            if (i == posicao and aux != None):
                return aux.info
        return 'Posição inválida'
    def destroi(self):
        self.inicio = None