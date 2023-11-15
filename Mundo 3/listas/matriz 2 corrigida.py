lista = [[0,0,0],[0,0,0],[0,0,0]]
pares = []
terceira = []
segunda  = []
lc = 0
cc = 0
for l in range(0,3):
    lc += 1
    for c in range(0,3):
        cc += 1
        lista[l][c] = int(input(f"digite um número para a linha {lc}, coluna {cc}: "))
        if cc == 3:
            cc = 0

print("-="*40)
for l in range(0,3):
    for c in range(0, 3):
        print("[",lista[l][c],"]", end='')
    print()


for l in range(0,3):
    for c in range(0,3):
        if lista[l][c]%2==0:
            pares.append(lista[l][c])

for l in range(0,3):
    terceira.append(lista[l][2])

for c in range(0,3):
    segunda.append(lista[1][c])

print("-="*40)
print("a soma dos números pares digitados é:",sum(pares))
print("a soma dos números digitados na terceira coluna é:",sum(terceira))
print("o maior número da segunda linha é:",max(segunda))
