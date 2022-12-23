from ListasEncadeadas import *

class Tabela:
    def __init__(self, Max = 7):
        self.vetor = [None] * (Max * 2 + 1)
        self.tamanho = 0

    def imprimir(self):
        for i in range(0, len(self.vetor)):
            if self.vetor[i] == None:
                print("Vazia")
            else:
                self.vetor[i].imprime()
                print('\n')

    def inserir(self, chave, info):
        posicao = (chave % 15)
        if self.vetor[posicao] == None:
            self.vetor[posicao] = ListaEncad()
        self.vetor[posicao].insere(chave, info)

    def consultar(self, chave):
        posicao = (chave % 15)
        if self.vetor[posicao] == None:
            return False
        return self.vetor[posicao].busca(chave)

    def excluir(self, chave):
        posicao = (chave % 15)
        if self.vetor[posicao] != None:
            self.vetor[posicao].exclui(chave)