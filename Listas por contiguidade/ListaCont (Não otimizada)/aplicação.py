from Produtos import Produtos
from Listacont import Lista

Produto1= Produtos("Arroz", 23)
Produto2= Produtos("Feijão",65)
Produto3= Produtos("Macarrão", 94)
Produto4= Produtos("Pipoca", 75)
Produto5= Produtos("Farinha", 45)
Produto6 = Produtos("Manteiga", 34)
lista=Lista(20)
lista.Inserir(1,Produto1)
lista.Inserir(2,Produto2)
lista.Inserir(3,Produto3)
lista.Inserir(4,Produto4)
lista.Inserir(5,Produto5)
lista.Inserir(6,Produto6)

print(lista)

lista.Excluir(3)

print(lista)
