class Nodo:
    def __init__(self, info):
        self.info = info
        self.prox = None
        self.ant = None
class ListaEncad:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tam = 0
    def vazia(self):
        return self.inicio == None
    def imprime(self):
        aux = self.inicio
        while aux != None:
            print('Item: '+ aux.info.getItem() + ', quantidade: ' + str(aux.info.getQuantidade()) + '\n')
            aux=aux.prox
        if self.vazia():
            print('Lista Vazia')
        print('\n')
    def imprimereverso(self):
        aux = self.fim
        while aux != None:
            print('Item: '+ aux.info.getItem() + ', quantidade: ' + str(aux.info.getQuantidade()) + '\n')
            aux=aux.ant
        if self.vazia():
            print('Lista vazia')
        print('\n')
    def exclui(self, posicao):
        if (not self.vazia() and posicao > 0):
            if posicao == 1:
                self.inicio = self.inicio.prox
                self.inicio.ant = None
                self.tam = self.tam - 1
                if self.tam == 0:
                    self.fim = None
            else:
                i=1
                aux = self.inicio
                auxant = None
                while (i < posicao and aux != None):
                    auxant = aux
                    aux = aux.prox
                    i = i +1
                if aux != None:
                    if aux == self.fim:
                        self.fim = auxant
                        auxant.prox = None
                        self.tam = self.tam - 1
                    else:
                        aux.prox.ant = auxant
                        auxant.prox = aux.prox
                        self.tam = self.tam - 1
    def insere(self, posicao, valor):
        if posicao > 0:
            novo = Nodo(valor)
            if posicao == 1:
                novo.prox = self.inicio
                self.inicio = novo
                self.tam = self.tam + 1
                if self.tam == 1:
                    self.fim = self.inicio
                else:
                    self.inicio.prox.ant = self.inicio
            else:
                aux = self.inicio
                i = 1
                while (i < posicao - 1 and aux != None):
                    aux = aux.prox
                    i = i + 1
                if aux != None:
                    if aux == self.fim:
                        aux.prox = novo
                        self.fim = novo
                        self.fim.ant = aux
                        self.tam = self.tam + 1
                    else:
                        novo.prox = aux.prox
                        aux.prox = novo
                        novo.prox.ant = novo
                        novo.ant = aux
                        self.tam = self.tam + 1
    def posicao(self, valor):
        aux = self.inicio
        i = 1
        while aux != None:
            if aux.info == valor:
                return i
            aux = aux.prox
            i = i + 1
        return 'Informação não encontrada'
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
        self.fim = None
        self.tam = 0
    def tamanho(self):
        return ('Tamanho da lista: ' + str(self.tam))
    def igualdade(self, segundalista):
        igual = True
        aux = self.inicio
        aux2 = segundalista.inicio
        while aux != None and aux2 != None:
            if aux.info != aux2.info:
                igual = False
            aux = aux.prox
            aux2 = aux2.prox
        if igual == True:
            print('Listas iguais')
        elif igual == False:
            print('Listas diferentes')