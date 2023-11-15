fator = int(input("digite um número para fatorar: "))
n = fator - 1

while n != 0:
    fator *= n
    n -= 1

print(fator)
