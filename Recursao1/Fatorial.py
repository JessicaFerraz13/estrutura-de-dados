def fatorial_iterativo(n):
    fatorial = 1
    while n > 0:
        fatorial = fatorial * n
        n = n - 1
    return fatorial

def fatorial_recursivo(n):
    if n == 0:
        return 1
    else:
        return n * fatorial_recursivo(n - 1)

n = 3

print(fatorial_iterativo(n))
print(fatorial_recursivo(n))