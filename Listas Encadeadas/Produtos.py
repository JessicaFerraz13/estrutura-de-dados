class Produtos:
    def __init__(self):
        self.item= None
        self.quantidade= None
    def __init__(self, item, quantidade):
        self.item=item
        self.quantidade=quantidade
    def __repr__(self):
        return "Item: " + self.item + ", Quantidade: " + str(self.quantidade)
    def getQuantidade(self):
        return self.quantidade
    def getItem(self):
        return self.item
    def setQuantidade(self,quantidade):
        self.quantidade=quantidade
    def setItem(self,item):
        self.item=item