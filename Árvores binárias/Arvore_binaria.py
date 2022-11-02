class Nodo:

    def __init__(self, info, esq=None, dir=None):
        self.info = info
        self.esq = esq
        self.dir = dir

    def __repr__(self):
        return str(self.info) + ' esq: ' + str(self.esq) + ' dir: ' + str(self.dir)

    def prefixesq(self):
        print(self.info, end= ' ')
        if self.esq:
            self.esq.prefixesq()
        if self.dir:
            self.dir.prefixesq()

    def infixesq(self):
        if self.esq:
            self.esq.infixesq()
        print(self.info, end= ' ')
        if self.dir:
            self.dir.infixesq()

    def posfixesq(self):
        if self.esq:
            self.esq.posfixesq()
        if self.dir:
            self.dir.posfixesq()
        print(self.info, end= ' ')

    def prefixdir(self):
        print(self.info, end= ' ')
        if self.dir:
            self.dir.prefixdir()
        if self.esq:
            self.esq.prefixdir()

    def infixdir(self):
        if self.dir:
            self.dir.infixdir()
        print(self.info, end=' ')
        if self.esq:
            self.esq.infixdir()

    def posfixdir(self):
        if self.dir:
            self.dir.posfixdir()
        if self.esq:
            self.esq.posfixdir()
        print(self.info, end= ' ')

    def localiza(self, valor, pilha = []):
        if self.info == valor:
            return self
        if len(pilha) > 0:
            pilha.pop()
        if self.dir:
            pilha.append(self.dir)
        if self.esq:
            pilha.append(self.esq)
        if len(pilha) > 0:
            return pilha[len(pilha) - 1].localiza(valor, pilha)

    def insere_esquerda(self, pai, filho):
        nodoPai = self.localiza(pai)
        if nodoPai != None and nodoPai.esq == None:
            nodoPai.esq = Nodo(filho)

    def insere_direita(self, pai, filho):
        nodoPai = self.localiza(pai)
        if nodoPai != None and nodoPai.dir == None:
            nodoPai.dir = Nodo(filho)

    def localiza_Pai(self, valor, pilha = []):
        if self.dir:
            if self.dir.info == valor:
                return self
        if self.esq:
            if self.esq.info == valor:
                return self
        if len(pilha) > 0:
            pilha.pop()
        if self.dir:
            pilha.append(self.dir)
        if self.esq:
            pilha.append(self.esq)
        if len(pilha) > 0:
            return pilha[len(pilha) - 1].localiza_Pai(valor, pilha)

    def folha(self):
        return self.esq == None and self.dir == None

    def remove_folha(self, valor):
        if self.info == valor:
            self.info = None
        else:
            nodoPai = self.localiza_Pai(valor)
            if nodoPai:
                if nodoPai.esq.info == valor and nodoPai.esq.folha():
                    nodoPai.esq = None
                if nodoPai.dir.info == valor and nodoPai.dir.folha():
                    nodoPai.dir = None