def fibonacci_iterativo(valor):
    if valor == 1 or valor == 2:
        fibonacci = 1
        return fibonacci
    else:
        i = 3
        fibonacci_ant = 1
        fibonacci = 2
        while i < valor:
            fibonacci_ant_ant = fibonacci_ant
            fibonacci_ant = fibonacci
            fibonacci = fibonacci + fibonacci_ant_ant
            i = i + 1
        return fibonacci

def fibonacci_recursivo(valor):
    if valor == 1 or valor == 2:
        return 1
    else:
        return fibonacci_recursivo(valor - 1) + fibonacci_recursivo(valor - 2)

n = 7

print(fibonacci_iterativo(n))
print(fibonacci_recursivo(n))

