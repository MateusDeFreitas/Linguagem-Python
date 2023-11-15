import random
import time

eu = input("pedra, papel ou tesoura? ")
ele = ["pedra", "papel", "tesoura"]
elemento = random.choice(ele)
print(elemento)

time.sleep(2)

if eu == "pedra" and elemento == "pedra":
    print("deu empate")
elif eu == "pedra" and elemento == "papel":
    print("o programa ganhou")
elif eu == "pedra" and elemento == "tesoura":
    print("eu ganhei")


elif eu == "papel" and elemento == "papel":
    print("deu empate")
elif eu == "papel" and elemento == "pedra":
    print("eu ganhei")
elif eu == "papel" and elemento == "tesoura":
    print("o programa ganhou")


elif eu == "tesoura" and elemento == "tesoura":
    print("deu empate")
elif eu == "tesoura" and elemento == "papel":
    print("eu ganhei")
elif eu == "tesoura" and elemento == "pedra":
    print("o programa ganhou")


else:
    print("lance inválido")
