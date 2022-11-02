class Clientes:
    def __init__(self, cpf, nome, profissao):
        self.cpf = cpf
        self.nome = nome
        self.profissao = profissao
    def __repr__(self):
        return "CPF: " + str(self.cpf) + ", Nome: " + self.nome + ', Profissão: ' + self.profissao