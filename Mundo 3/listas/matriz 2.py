lista = []
pares = []
terceira = []
segunda  = []

a = int(input("digite um número para [0,0]: "))
b = int(input("digite um número para [0,1]: "))
c = int(input("digite um número para [0,2]: "))
d = int(input("digite um número para [1,0]: "))
e = int(input("digite um número para [1,1]: "))
f = int(input("digite um número para [1,2]: "))
g = int(input("digite um número para [2,0]: "))
h = int(input("digite um número para [2,1]: "))
i = int(input("digite um número para [2,2]: "))

lista.append(a)
lista.append(b)
lista.append(c)
lista.append(d)
lista.append(e)
lista.append(f)
lista.append(g)
lista.append(h)
lista.append(i)

terceira.append(c)
terceira.append(f)
terceira.append(i)

segunda.append(d)
segunda.append(e)
segunda.append(f)

print("-="*40)
print("[",lista[0],"]","[",lista[1],"]","[",lista[2],"]")
print("[",lista[3],"]","[",lista[4],"]","[",lista[5],"]")
print("[",lista[6],"]","[",lista[7],"]","[",lista[8],"]")

for n in lista:
    if n%2==0:
        pares.append(n)

print("a soma dos números pares digitados é:",sum(pares))
print("a soma dos números digitados na terceira coluna é:",sum(terceira))
print("o maior número da segunda linha é:",max(segunda))