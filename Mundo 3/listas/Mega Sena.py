from random import randint

vezes   = int(input("quantos jogos serão feitos? "))
cont    = 0
numeros = []
jogada  = []

while cont != vezes:
    while len(jogada) != 6:
        n = randint(1,60)
        if n not in jogada:
            jogada.append(n)
    numeros.append(jogada[:])
    jogada.clear()
    print("-+"*20)
    print(sorted(numeros[cont]))
    cont += 1