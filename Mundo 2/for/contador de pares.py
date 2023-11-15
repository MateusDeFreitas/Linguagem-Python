num   = int(input("digite o número do início do intervalo: "))
ext   = int(input("digite o tamanho do intervalo: "))
par   = []
impar = []

for n in range(num, num+ext):
    if (n%2) == 0:
        par.append(n)
    else:
        impar.append(n)


print()
print("os números pares desse intervalo são:",par)
soma = sum(par)
print("A soma dos números pares desse intervalo é",soma)
print()
print("os números impares desse intervalo são:",impar)
soma2 = sum(impar)
print("A soma dos números impares desse intervalo é",soma2)