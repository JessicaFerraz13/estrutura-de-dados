class Clientes:
    def __init__(self, numero, nome):
        self.numero = numero
        self.nome = nome
    def __repr__(self):
        return "Número: " + str(self.numero) + ", Nome: " + self.nome
    def getnumero(self):
        return self.numero
    def getnome(self):
        return self.nome