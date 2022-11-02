def soma_digitos(numero):
    Numeros = list(str(numero))
    if len(Numeros) == 1:
        return int(Numeros[0])
    else:
        return int(Numeros[0]) + soma_digitos(int(''.join(Numeros[1:])))

print(soma_digitos(732))
