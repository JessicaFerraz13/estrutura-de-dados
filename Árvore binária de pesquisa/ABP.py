class Nodo:

    def __init__(self, chave = None, info = None):
        self.chave = chave
        self.info = info
        self.esq = None
        self.dir = None

    def imprime(self):
        print(self.info)
        if self.esq:
            self.esq.imprime()
        if self.dir:
            self.dir.imprime()

    def inserir(self, chave, info):
        if self.chave == None:
            self.chave = chave
            self.info = info
        elif chave < self.chave:
            if self.esq:
                return self.esq.inserir(chave, info)
            self.esq = Nodo(chave, info)
        elif chave > self.chave:
            if self.dir:
                return self.dir.inserir(chave, info)
            self.dir = Nodo(chave, info)
        elif chave == self.chave:
            self.info = info

    def buscar(self, chave):
        if self.chave == None:
            return None
        elif chave < self.chave:
            if self.esq:
                return self.esq.buscar(chave)
        elif chave > self.chave:
            if self.dir:
                return self.dir.buscar(chave)
        elif chave == self.chave:
            return self

    def buscar_pai(self, chave):
        if self.chave == None:
            return None
        elif chave == self.esq.chave:
            return self, True
        elif chave == self.dir.chave:
            return self, False
        elif chave < self.chave:
            if self.esq:
                return self.esq.buscar_pai(chave)
        elif chave > self.chave:
            if self.dir:
                return self.dir.buscar_pai(chave)

    def folha(self):
        return self.esq == None and self.dir == None

    def excluir(self, chave):
        nodo = self.buscar(chave)
        nodo_pai, esquerda = self.buscar_pai(chave)
        if nodo.folha():
            if esquerda:
                nodo_pai.esq = None
            else:
                nodo_pai.dir = None
