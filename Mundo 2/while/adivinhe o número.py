from random import randint

n = randint(0,10)
tentativas = 0

tentativa = int(input("tente aivinhar o número entre 0 e 10 escolhido pelo computador: "))
while tentativa != n:
    tentativa = int(input("tente denovo: "))
    tentativas += 1
print("parabéns você acertou após",tentativas,"tentativas")



