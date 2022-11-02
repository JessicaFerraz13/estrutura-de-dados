class Clientes:
    def __init__(self, cpf, nome, profissao):
        self.cpf = cpf
        self.nome = nome
        self.profissao = profissao

    def __repr__(self):
        return "CPF: " + str(self.cpf) + ", Nome: " + self.nome + ', Profissão: ' + self.profissao

    def getcpf(self):
        return self.cpf

    def getnome(self):
        return self.nome

    def getprofissao(self):
        return self.profissao

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
                string = string + str(self.chave[i]) + ': ' + str(self.valor[i]) + '\n'
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

    def buscalinear(self, chave, indice):
        if self.chave[indice] == chave:
            return 1
        elif self.chave[indice] is not None:
            return self.buscalinear(chave, indice + 1)
        return 0

    def buscabinaria(self, chave, inicio, fim):
        meio = (inicio + fim) // 2
        if self.chave[meio] == chave:
            return meio
        elif inicio < fim:
            if self.chave[meio] < chave:
                return self.buscabinaria(chave, meio + 1, fim)
            elif self.chave[meio] > chave:
                return self.buscabinaria(chave, inicio, meio - 1)
        else:
            return 0

    def buscar(self, chave, opcao):
        if opcao == 'l':
            if not self.vazia():
                return self.buscalinear(chave, self.inicio)
            return 0
        elif opcao == 'b':
            if not self.vazia():
                return self.buscabinaria(chave, self.inicio, self.fim)
            return 0
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

Cliente1 = Clientes(34856092384, 'João', 'Arquiteto')
Cliente2 = Clientes(20968594883, 'Maria', 'Engenheira de Computação')
Cliente3 = Clientes(95849032540, 'Fernando', 'Agricultor')
Cliente4 = Clientes(54930495321, 'Robson', 'Engenheiro Químico')
Cliente5 = Clientes(19325697834, 'Andressa', 'Manicure')
Cliente6 = Clientes(79845093456, 'Osvaldo', 'Pedreiro')
Cliente7 = Clientes(89543068934, 'Jeferson', 'Açogueiro')
Cliente8 = Clientes(56790987432, 'Fabíola', 'Advogada')
Cliente9 = Clientes(38930569832, 'Mercedes', 'Jornalista')
Cliente10 = Clientes(60945932053, 'Ana', 'Economista')

Tabela = Tabela(10)

Tabela.inserir(Cliente1.cpf, Cliente1)
Tabela.inserir(Cliente2.cpf, Cliente2)
Tabela.inserir(Cliente3.cpf, Cliente3)
Tabela.inserir(Cliente4.cpf, Cliente4)
Tabela.inserir(Cliente5.cpf, Cliente5)
Tabela.inserir(Cliente6.cpf, Cliente6)
Tabela.inserir(Cliente7.cpf, Cliente7)
Tabela.inserir(Cliente8.cpf, Cliente8)
Tabela.inserir(Cliente9.cpf, Cliente9)

print(Tabela)

print(Tabela.buscar(Cliente10.cpf, 'b'))
