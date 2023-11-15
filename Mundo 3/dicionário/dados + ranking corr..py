from random import randint
from operator import itemgetter
from time import sleep

jogo = {'jogador1':randint(1,6),
    'jogador2':randint(1,6),
    'jogador3':randint(1,6),
    'jogador4':randint(1,6)}
print("  == VALORES SORTEADOS! ==")
for k, v in jogo.items():
    print(f"{k} tirou {v} nos dasdos!")
    sleep(1)
print("=-"*40)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print("        ==RESULTADOS!==")
for i,v in enumerate(ranking):
     print(f"   {i+1} lugar: {v[0]} com {v[1]}")
     sleep(1)