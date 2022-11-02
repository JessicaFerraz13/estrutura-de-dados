from PilhaContiguidade import PilhaContiguidade as Pilha

Num1 = 43
Num2 = 65
Num3 = 94
Num4 = 75
Num5 = 45
Num6 = 34
Num7 = 21
Num8 = 12
Num9 = 24
Num10 = 43
Num11 = 65

pilha = Pilha()

pilha.empilha(Num1)
pilha.empilha(Num2)
pilha.empilha(Num3)
pilha.empilha(Num4)
pilha.empilha(Num5)

print(pilha.consultar())

pilha.empilha(Num6)
pilha.empilha(Num7)
pilha.empilha(Num8)
pilha.empilha(Num9)
pilha.empilha(Num10)
pilha.empilha(Num11)

print(pilha.consultar())

pilha.desempilha()
print(pilha.consultar())

print(pilha.vazia())

pilha.destroi()
print(pilha.vazia())