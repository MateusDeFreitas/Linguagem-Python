parar   = ' '
números = []

while parar != 'parar':
    x = int(input("digite um número: "))
    if x not in números:
        números.append(x)
    parar = input("se desejar interromper o programa digite 'parar': ")

print('-'*40)
print("Os números listados são:",sorted(números))
