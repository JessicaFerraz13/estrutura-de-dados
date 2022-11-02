from FilaContiguidade import FilaContiguidade as Fila
from PilhaContiguidade import PilhaContiguidade as Pilha

Num1 = 43
Num2 = 65
Num3 = 94
Num4 = 75
Num5 = 45
Num6 = 34
Num7 = 21
Num8 = 65
Num9 = 24
Num10 = 42

fila = Fila(20)

fila.insere(Num1)
fila.insere(Num2)
fila.insere(Num3)
fila.insere(Num4)
fila.insere(Num5)
fila.insere(Num6)
fila.insere(Num7)
fila.insere(Num8)
fila.insere(Num9)
fila.insere(Num10)

def ordenacao(fila):
    pilha1 = Pilha(fila.tamanho)
    pilha2 = Pilha(fila.tamanho)
    while not fila.vazia():
        if not pilha1.vazia():
            if fila.consulta() <= pilha1.consultar():
                pilha1.empilha(fila.consulta())
                fila.remove()
                while not pilha2.vazia():
                    pilha1.empilha(pilha2.consultar())
                    pilha2.desempilha()
            else:
                pilha2.empilha(pilha1.consultar())
                pilha1.desempilha()
        else:
            pilha1.empilha(fila.consulta())
            fila.remove()
            while not pilha2.vazia():
                pilha1.empilha(pilha2.consultar())
                pilha2.desempilha()
    while not pilha1.vazia():
        fila.insere(pilha1.consultar())
        pilha1.desempilha()
    return fila

print(ordenacao(fila))