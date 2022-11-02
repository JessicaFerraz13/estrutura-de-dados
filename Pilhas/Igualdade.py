from PilhaContiguidade import PilhaContiguidade as Pilha
#from PilhaEncadeamento import PilhaEncadeamento as Pilha

#No arquivo de pilha por contiguidade fisica atruibui o valor maximo como 10 para as duas funcionarem
#do mesmo jeito, sem alterar nada.

Num1 = 54
Num2 = 95
Num3 = 32
Num4 = 3

pilha1 = Pilha()
pilha1.empilha(Num1)
pilha1.empilha(Num2)
pilha1.empilha(Num3)

pilha2 = Pilha()
pilha2.empilha(Num1)
pilha2.empilha(Num2)
pilha2.empilha(Num4)


def igualdade(pilha1, pilha2):
    topo1 = pilha1.consultar()
    topo2 = pilha2.consultar()
    pilhaaux1 = Pilha()
    pilhaaux2 = Pilha()
    igual = True
    while topo1 != None and topo2 != None:
        if topo1 != topo2:
            igual = False
        pilhaaux1.empilha(topo1)
        pilhaaux2.empilha(topo2)
        pilha1.desempilha()
        pilha2.desempilha()
        topo1 = pilha1.consultar()
        topo2 = pilha2.consultar()
    if topo1 != None or topo2 != None:
        igual = False
    topo1 = pilhaaux1.consultar()
    topo2 = pilhaaux2.consultar()
    while topo1 != None and topo2 != None:
        pilha1.empilha(topo1)
        pilha2.empilha(topo2)
        pilhaaux1.desempilha()
        pilhaaux2.desempilha()
        topo1 = pilhaaux1.consultar()
        topo2 = pilhaaux2.consultar()
    return igual

print(igualdade(pilha1, pilha2))

print(pilha1.consultar())
print(pilha2.consultar())

pilha2.desempilha()
print(pilha1.consultar())
print(pilha2.consultar())