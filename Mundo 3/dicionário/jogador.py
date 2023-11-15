nome = input("Digite o none do jogador: ")
part = int(input(f"Quantas partidas {nome} jogou: "))
cont = 1
gols = []
while cont-1 != part:
    qgol = int(input(f"Quantos gols {nome}, fez na {cont}º partida: "))
    gols.append(qgol)
    cont += 1

jogador = {'nome':nome,'Número de partidas':part,
           'Gols feitos':gols,'Total de gols':sum(gols)}

print("=-"*40)
print("O jogador selecionado é:",jogador['nome'])
print("O",jogador['nome'],"jogou",jogador['Número de partidas'],"partidas")
print("No total",jogador['nome'],"fez",jogador['Total de gols'],"gols")
