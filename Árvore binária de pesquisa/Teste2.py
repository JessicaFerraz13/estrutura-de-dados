from ABP import *
from Clientes import *

no1 = 500
no2 = 300
no3 = 800
no4 = 150
no5 = 400
no6 = 600
no7 = 900
no8 = 380
no9 = 750

Arvore = Nodo()

Arvore.inserir(no1, no1)
Arvore.inserir(no2, no2)
Arvore.inserir(no3, no3)
Arvore.inserir(no4, no4)
Arvore.inserir(no5, no5)
Arvore.inserir(no6, no6)
Arvore.inserir(no7, no7)


Arvore.imprime()
Arvore.excluir(900)
Arvore.imprime()