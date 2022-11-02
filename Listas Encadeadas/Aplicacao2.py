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

print(lista.posicao(Produto5))

print(lista.valor(2))