jogadores = []

while True:
    nome = input("digite o nome do jogador (ou '0' para parar): ")
    if nome == '0':
        break
    part = int(input(f"Quantas partidas {nome} jogou: "))
    cont = 1
    gols = []
    while cont - 1 != part:
        qgol = int(input(f"Quantos gols {nome}, fez na {cont}º partida: "))
        gols.append(qgol)
        cont += 1
    jogador = {'nome':nome,'Nº de partidas':part,'gols':gols[:],'total de gols':sum(gols)}
    jogadores.append(jogador.copy())
    jogador.clear()
    gols.clear()
    cont = 1

print("-="*50)
for jogador in jogadores:
    print("=-" * 40)
    print("O jogador selecionado é:", jogador['nome'])
    print("O", jogador['nome'], "jogou", jogador['Nº de partidas'], "partidas")
    print("No total", jogador['nome'], "fez", jogador['total de gols'], "gols")
    print("=-" * 40)
    cont2 = 1
    cont3 = 0
    while len(jogador['gols']) != cont3:
        print(f"o {jogador['nome']}, fez {jogador['gols'][cont2-1]} gols na {cont2}º partida: ")
        cont2 += 1
        cont3 += 1
