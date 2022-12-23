from TabelaHash import *
from Clientes import *

Cliente1 = Clientes(73, 'João')
Cliente2 = Clientes(15, 'Carlos')
Cliente3 = Clientes(44, 'Marcia')
Cliente4 = Clientes(37, 'Ronaldo')
Cliente5 = Clientes(30, 'Michel')
Cliente6 = Clientes(59, 'Darci')
Cliente7 = Clientes(61, 'Joana')
Cliente8 = Clientes(99, 'Denise')

tab = Tabela()
tab.inserir(Cliente1.numero, Cliente1)
tab.inserir(Cliente2.numero, Cliente2)
tab.inserir(Cliente3.numero, Cliente3)
tab.inserir(Cliente4.numero, Cliente4)
tab.inserir(Cliente5.numero, Cliente5)
tab.inserir(Cliente6.numero, Cliente6)
tab.inserir(Cliente7.numero, Cliente7)
tab.inserir(Cliente8.numero, Cliente8)

tab.imprimir()