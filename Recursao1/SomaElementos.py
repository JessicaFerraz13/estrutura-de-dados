def soma_elementos_iterativo(v):
    soma = 0
    for i in range(0, len(v)):
        soma = soma + v[i]
    return soma

def soma_elementos_recursivo(v):
    if len(v) == 1:
        return v[0]
    else:
        return v[0] + soma_elementos_recursivo(v[1:])

v = [1, 2, 3, 10]

print(soma_elementos_iterativo(v))
print(soma_elementos_recursivo(v))