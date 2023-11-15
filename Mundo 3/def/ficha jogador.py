def ficha(nome="<desconhecido>",gol=0):
    print("=-" * 40)
    print(f"o jogador {nome} fez {gol} gols")
    print("=-" * 40)


n = str(input("digite o nome do jogador: "))
g = str(input(f"digite quantos gols {n} fez: "))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n,g)


