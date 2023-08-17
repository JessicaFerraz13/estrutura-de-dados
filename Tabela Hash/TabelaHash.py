from ListasEncadeadas import *

class Tabela:
    def __init__(self, Max = 29):
        self.vetor = [None] * (Max + 1)
        self.tamanho = 0

    def imprimir(self): # Apenas para visualizar se esta funcionando corretamente
        for i in range(1, len(self.vetor)):
            if self.vetor[i] == None:
                print("Vazia")
            else:
                self.vetor[i].imprime()
                print('\n')

    def inserir(self, chave, info):
        posicao = (chave % Max) + 1
        if self.vetor[posicao] == None:
            self.vetor[posicao] = ListaEncad()
        self.vetor[posicao].insere(chave, info)

    def consultar(self, chave):
        posicao = (chave % Max) + 1
        if self.vetor[posicao] == None:
            return False
        return self.vetor[posicao].busca(chave)

    def excluir(self, chave):
        posicao = (chave % Max) + 1
        if self.vetor[posicao] != None:
            self.vetor[posicao].exclui(chave)
