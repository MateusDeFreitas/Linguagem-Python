numeros = []
parar = 'não'

while parar != 'sim':
    n1 = int(input("digite um número: "))
    numeros.append(n1)
    n2 = int(input("digite um número: "))
    numeros.append(n2)
    n3 = int(input("digite um número: "))
    numeros.append(n3)
    n4 = int(input("digite um número: "))
    numeros.append(n4)
    n5 = int(input("digite um número: "))
    numeros.append(n5)
    parar = input("para parar o programa digite 'sim' ")

soma = sum(numeros)
media = soma /len(numeros)

print(soma)
print(media)