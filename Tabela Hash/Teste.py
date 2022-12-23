from Tabela import *
from Clientes import *

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
Tabela.inserir(Cliente10.cpf, Cliente10)

print(Tabela)

print(Tabela.buscar(Cliente6.cpf, 'b'))

print(Tabela.valor)
