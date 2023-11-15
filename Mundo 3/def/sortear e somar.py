from random import randint

numeros = []
def sorteio(numero_de_sorteios):
    cont = numero_de_sorteios
    while cont != 0:
        x = randint(0,100)
        numeros.append(x)
        cont -= 1
    print(numeros)


pares = []
def somarPar(lista):
    for n in lista:
        if n % 2 == 0:
            pares.append(n)
    print("a soma dos números pares sorteados é:",sum(pares))



sorteio(5)
somarPar(numeros)