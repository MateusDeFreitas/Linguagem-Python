lista = []

menor  = 0
pmenor = [0]
maior  = 0
pmaior = [0]

lista.append(int(input('Digite um número: ')))
lista.append(int(input('Digite um número: ')))
lista.append(int(input('Digite um número: ')))
lista.append(int(input('Digite um número: ')))
lista.append(int(input('Digite um número: ')))


for c, n in enumerate(lista):
    if c == 0 or n > maior:
        pmaior.clear()
        maior = n
        pmaior.append(c)
    elif n == maior:
        pmaior.append(c)
    if c == 0 or n < menor:
        pmenor.clear()
        menor = n
        pmenor.append(c)
    elif n == menor:
        pmenor.append(c)

print('---------------------------------------------------')
print(f"A lista inserida é: {lista}")
print()

print(f"o maior número listado foi {maior} ele esta na {pmaior} posição")
print(f"o menor número listado foi {menor} ele esta na {pmenor} posição")
print('---------------------------------------------------')