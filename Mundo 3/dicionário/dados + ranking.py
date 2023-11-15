from random import randint
jogadores = []
numeros   = []
ranking   = []


for i in range(1,5):
    nome = input("digite o nome: ")
    dado = randint(1,6)
    jogador = {"nome":nome,"número":dado}
    jogadores.append(jogador.copy())

cont = 0
for i in jogadores:
    numeros.append(jogadores[cont]['número'])
    cont += 1

print("-="*30)
cont1 = 0
for i in jogadores:
    print("O jogador",jogadores[cont1]['nome'],"tirou",jogadores[cont1]['número'])
    cont1 += 1


cont2 = 0
for jogador in jogadores:
    if cont2 == 0:
        ranking.append(jogador)
    elif cont2 == 1:
        if jogador['número'] < ranking[0]['número']:
            ranking.insert(0,jogador)
        else:
            ranking.append(jogador)
    elif cont2 == 2:
        if jogador['número'] > ranking[-1]['número']:
            ranking.append(jogador)
        elif jogador['número'] > ranking[-2]['número']:
            ranking.insert(-2,jogador)
        else:
            ranking.insert(0,jogador)
    else:
        if jogador['número'] > ranking[-1]['número']:
            ranking.append(jogador)
        elif jogador['número'] > ranking[-2]['número']:
            ranking.insert(-2,jogador)
        elif jogador['número'] > ranking[-3]['número']:
            ranking.insert(-3, jogador)
        else:
            ranking.insert(0,jogador)
    cont2 += 1

print("-="*30)
cont3 = 3
cont4 = 1
for i in ranking:
    print("O jogador",ranking[cont3]['nome'],"tirou",ranking[cont3]['número'])
    print("Ele ficou na",cont4,"colocação")
    print()
    cont3 -= 1
    cont4 += 1