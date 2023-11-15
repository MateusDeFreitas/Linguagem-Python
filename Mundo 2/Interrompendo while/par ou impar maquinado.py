from random import randint

escolha = input('"par" ou "impar"? ')
n  = randint(0,51)
n2 = int(input("digite um número: "))
n3 = n + n2
resultado = 'x'
cont = 0


while True:
    if escolha == 'par':
        print("----------------------------------------------------------")
        print("você escolheu par")
        print("o computador escolheu impar")
        print("você escolheu o número: ",n2)
        print("o computador escolheu o número", n)
        print("a soma é",n3)
        if n3 % 2 == 0:
            print("o resultado é par, você ganhou")
            cont += 1
            print("----------------------------------------------------------")
            escolha = input('"par" ou "impar"? ')
            n = randint(0, 51)
            n2 = int(input("digite um número: "))
            n3 = n + n2
        else:
            print("o resultado é impar, o computador ganhou")
            print("----------------------------------------------------------")
            break
    elif escolha == 'impar':
        print("----------------------------------------------------------")
        print("você escolheu impar")
        print("o computador escolheu par")
        print("você escolheu o número: ",n2)
        print("o computador escolheu o número", n)
        print("a soma é", n3)
        if n3 % 2 == 0:
            print("o resultado é par, o computador ganhou")
            print("----------------------------------------------------------")
            break
        else:
            print("o resultado é impar, você ganhou")
            cont += 1
            print("----------------------------------------------------------")
            escolha = input('"par" ou "impar"? ')
            n = randint(0, 51)
            n2 = int(input("digite um número: "))
            n3 = n + n2



if cont >= 2:
    print("vecê ganhou",cont,"vezes consecutivas")
elif cont == 1:
    print("vecê ganhou", cont,"vez")
else:
    print("vecê não ganhou nenhuma vez")



