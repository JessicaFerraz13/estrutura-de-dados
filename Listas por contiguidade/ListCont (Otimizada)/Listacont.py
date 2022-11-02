class Lista:
    def __init__(self,max):
        self.max=max
        self.vetor=[None]*self.max
        self.ini=-1
        self.fim=-1
    def __repr__(self):
        string= "[Ini "
        for i in range(self.ini,self.fim+1):
            string=string+" --> " + str(self.vetor[i])
        return string + "]"
    def Vazia(self):
        return self.ini==-1 or self.fim==-1
    def Tamanho(self):
        if self.Vazia():
            return 0
        else:
            return self.fim-self.ini+1
    def Inserir(self,posicao,dado):
        if ((self.ini != 0 or self.fim != self.max -1) and posicao>0 and posicao <= self.Tamanho()+1):
            if (self.Vazia()):
                self.ini=self.max//2
                self.fim=self.max//2
            elif (self.ini == 0 or (posicao > self.Tamanho() // 2 and self.fim != self.max - 1)):
                for i in range(self.fim,self.ini+posicao-2,-1):
                    self.vetor[i+1]=self.vetor[i]
                self.fim=self.fim+1
            else:
                for i in range(self.ini,self.ini+posicao-1):
                    self.vetor[i-1]=self.vetor[i]
                self.ini=self.ini-1
            self.vetor[self.ini+posicao-1]=dado
            return True
        else:
            return False
    def Consultar(self, posicao):
        if not self.Vazia():
            return self.vetor[self.ini+posicao-1]
    def Limpar(self):
        self.ini=-1
        self.fim=-1
    def Excluir(self,posicao):
        if ((not self.Vazia()) and posicao>0 and posicao <= self.Tamanho()):
            if (posicao > (self.Tamanho()//2)):
                for i in range(self.ini+posicao, self.fim+1):
                    self.vetor[i-1]=self.vetor[i]
                self.fim=self.fim-1
            else:
                for i in range(self.ini+posicao-2,self.ini-1,-1):
                    self.vetor[i+1]=self.vetor[i]
                self.ini=self.ini+1
            return True
        else:
            return False
