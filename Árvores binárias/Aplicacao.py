from Arvore_binaria import *

Raiz = Nodo('a')
Raiz.esq = Nodo('b')
Raiz.dir = Nodo('c')
Raiz.esq.esq = Nodo('d')
Raiz.esq.dir = Nodo('e')
Raiz.dir.esq = Nodo('f')
Raiz.dir.dir = Nodo('g')

print(Raiz.localiza('g'))

Raiz.prefixdir()

Raiz.insere_direita('f', 'h')

print('\n\n')

Raiz.posfixesq()




