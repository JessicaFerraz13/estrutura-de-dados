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