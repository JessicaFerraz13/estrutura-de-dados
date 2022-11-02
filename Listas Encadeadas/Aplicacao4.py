from Produtos import Produtos
from ListasEncadeadas import ListaEncad

Produto1= Produtos("Arroz", 23)
Produto2= Produtos("Feijão", 65)
Produto3= Produtos("Macarrão", 94)
Produto4= Produtos("Pipoca", 75)
Produto5= Produtos("Farinha", 45)
Produto6= Produtos("Manteiga", 34)

lista=ListaEncad()

lista.insere(1,Produto1)
lista.insere(2,Produto2)
lista.insere(3,Produto3)
lista.insere(3,Produto4)
lista.insere(5,Produto5)
lista.insere(1,Produto6)

lista2 = ListaEncad()

lista2.insere(1,Produto1)
lista2.insere(2,Produto2)
lista2.insere(3,Produto3)
lista2.insere(3,Produto4)
lista2.insere(5,Produto5)
lista2.insere(1,Produto6)
lista2.exclui(2)

lista3 = ListaEncad()

lista3.insere(1,Produto1)
lista3.insere(2,Produto2)
lista3.insere(3,Produto3)
lista3.insere(3,Produto4)
lista3.insere(5,Produto5)
lista3.insere(1,Produto6)

lista.igualdade(lista2)

lista.igualdade(lista3)