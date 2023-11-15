lista = [[0,0,0],[0,0,0],[0,0,0]]
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

