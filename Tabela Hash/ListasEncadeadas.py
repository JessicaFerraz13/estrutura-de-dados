class Nodo:
    def __init__(self, chave, info):
        self.info = info
        self.chave = chave
        self.prox = None
class ListaEncad:
    def __init__(self):
        self.inicio = None

    def imprime(self):
        aux = self.inicio
        while aux != None:
            print('Número: '+ str(aux.info.getnumero()) + ', Nome: ' + aux.info.getnome(), end="   ")
            aux=aux.prox

    def exclui(self, chave):
        if chave == self.inicio.chave:
            self.inicio = self.inicio.prox
        else:
            aux = self.inicio
            ant = None
            while (chave != aux.chave and aux != None):
                ant = aux
                aux = aux.prox
            if aux != None:
                ant.prox = aux.prox
    
    def insere(self, chave, info):
        novo = Nodo(chave, info)
        novo.prox = self.inicio
        self.inicio = novo

    def busca(self, chave):
        aux = self.inicio
        while aux != None:
            if aux.chave == chave:
                return aux.info
            aux = aux.prox
        return False