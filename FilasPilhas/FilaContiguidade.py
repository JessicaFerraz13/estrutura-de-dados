class FilaContiguidade:
    def __init__(self, tamanho):
        self.LS = tamanho - 1
        self.LI = 0
        self.vetor = [None] * tamanho
        self.inicio = self.LI - 1
        self.fim = self.LS + 1
        self.tamanho = 0
    def __repr__(self):
        string = '['
        if not self.vazia():
            if self.inicio <= self.fim:
                for i in range(self.inicio, self.fim + 1):
                    string = string + ' --> ' + str(self.vetor[i])
            else:
                for i in range(self.inicio, self.LS + 1):
                    string = string + ' --> ' + str(self.vetor[i])
                for i in range(self.LI, self.fim + 1):
                    string = string + ' --> ' + str(self.vetor[i])
        return string + ']'
    def vazia(self):
        return self.inicio < self.LI and self.fim > self.LS
    def cheia(self):
        return (self.inicio == self.LI and self.fim == self.LS) or (self.fim + 1 == self.inicio)
    def insere(self,dado):
        if self.vazia():
            self.inicio = self.LI
            self.fim = self.LI
            self.vetor[self.fim] = dado
            self.tamanho = self.tamanho + 1
        elif not self.cheia():
            if self.fim == self.LS:
                self.fim = self.LI
            else:
                self.fim = self.fim + 1
            self.vetor[self.fim] = dado
            self.tamanho = self.tamanho + 1
    def consulta(self):
        if not self.vazia():
            return self.vetor[self.inicio]
    def destroi(self):
        self.inicio = self.LI - 1
        self.fim = self.LS + 1
        self.tamanho = 0
    def remove(self):
        if not self.vazia():
            if self.inicio > self.fim and self.inicio == self.LS:
                self.inicio = self.LI
                self.tamanho = self.tamanho - 1
            elif self.inicio == self.fim:
                self.destroi()
            else:
                self.inicio = self.inicio + 1
                self.tamanho = self.tamanho - 1