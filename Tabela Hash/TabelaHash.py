from ListasEncadeadas import *

class Tabela:
    def __init__(self, Max = 20):
        self.vetor = [None] * (Max * 2)
        self.tamanho = 0

    def inserir(self, chave, valor):
        posicao = chave % 27
        if self.vetor[posicao] != None:


    def consultar(self, chave):
        posicao = self.buscar(chave, 'b')
        if posicao > 0:
            return self.valor[posicao]

    def excluir(self, chave):
        posicao = self.buscar(chave, 'b')
        if posicao > 0:
            for i in range(posicao, self.fim):
                self.chave[i] = self.chave[i + 1]
                self.valor[i] = self.valor[i + 1]
            self.fim = self.fim - 1

    def destruir(self):
        self.inicio = self.LI - 1
        self.fim = self.LS + 1