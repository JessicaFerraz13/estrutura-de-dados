class Nodo:
    def __init__(self, info):
        self.info = info
        self.prox = None
class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def vazia(self):
        return self.inicio == None

    def imprime(self):
        aux = self.inicio
        while aux != None:
            print('Número: '+ str(aux.info))
            aux = aux.prox
            print('\n')

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
        return self.posicao_aux(valor, 1, self.inicio)

    def posicao_aux(self, valor, indice, aux):
        if aux == None:
            return 0
        elif aux.info == valor:
            return indice
        else:
            return self.posicao_aux(valor, indice + 1, aux.prox)

    def valor(self, posicao):
        return self.valor_aux(posicao, 1, self.inicio)

    def valor_aux(self, posicao, indice, aux):
        if aux == None:
            return None
        elif indice == posicao:
            return aux.info
        else:
            return self.valor_aux(posicao, indice + 1, aux.prox)

    def destroi(self):
        self.inicio = None

num1 = 23
num2 = 84
num3 = 34
num4 = 47
num5 = 21
num6 = 95
num7 = 32
num8 = 1
num9 = 14
num10 = 2

lista = ListaEncadeada()
lista.insere(1, num1)
lista.insere(2, num2)
lista.insere(2, num3)
lista.imprime()
print(lista.posicao(34))
print(lista.valor(1))

