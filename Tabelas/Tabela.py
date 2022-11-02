class Tabela:
    def __init__(self, Max):
        self.chave = [None] * (Max + 1)
        self.valor = [None] * (Max + 1)
        self.LI = 1
        self.LS = Max
        self.inicio = self.LI - 1
        self.fim = self.LS + 1

    def __repr__(self):
        string = ''
        if not self.vazia():
            for i in range(self.inicio, self.fim + 1):
                string = string + str(self.valor[i]) + '\n'
        return string + '\n'

    def vazia(self):
        return self.inicio < self.LI or self.fim > self.LS

    def cheia(self):
        return (self.inicio == self.LI and self.fim == self.LS)

    def tamanho(self):
        if not self.vazia():
            return self.fim - self.inicio + 1
        else:
            return 0

    def buscalinear(self, chave):
        if not self.vazia():
            for i in range(self.inicio, self.fim + 1):
                if self.chave[i] == chave:
                    return i
        return 0

    def buscabinaria(self, chave):
        if not self.vazia():
            inicio = self.inicio
            fim = self.fim
            while inicio < fim:
                meio = (inicio + fim) // 2
                if chave > self.chave[meio]:
                    inicio = meio + 1
                elif chave < self.chave[meio]:
                    fim = meio - 1
                elif chave == self.chave[meio]:
                    posicao = meio
                    return posicao
        return 0

    def buscar(self, chave, opcao):
        if opcao == 'l':
            posicao = self.buscalinear(chave)
            return posicao
        elif opcao == 'b':
            posicao = self.buscabinaria(chave)
            return posicao
        return 0

    def inserir(self, chave, valor):
        posicao = self.buscar(chave, 'b')
        if posicao > 0:
            self.valor[posicao] = valor
        elif not self.cheia():
            if self.vazia():
                self.inicio = self.LI
                self.fim = self.LI
                self.chave[self.inicio] = chave
                self.valor[self.inicio] = valor
            else:
                self.fim = self.fim + 1
                posicao = self.LI
                while self.chave[posicao] < chave:
                    posicao = posicao + 1
                    if posicao == self.fim:
                        break
                for i in range(self.fim, posicao, -1):
                    self.chave[i] = self.chave[i - 1]
                    self.valor[i] = self.valor[i - 1]
                self.chave[posicao] = chave
                self.valor[posicao] = valor

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