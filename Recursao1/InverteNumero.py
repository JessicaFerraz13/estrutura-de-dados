def inverte(n):
    if n < 10:
        return n
    return str(n % 10) + str(inverte(n // 10))  

n = 12345
print(inverte(n))
