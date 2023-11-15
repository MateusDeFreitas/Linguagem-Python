n1 = int(input("digite um valor: "))
n2 = int(input("digite outro valor: "))

print("[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair de programa")

ope = int(input("qual operação devo realizar?: "))

while not ope == 5:
    if ope == 1:
        print(" a soma dos valores é",n1 + n2)
    elif ope == 2:
        print(" a multiplicação dos valores é", n1 * n2)
    elif ope == 3:
        if n1 > n2:
            print(n1)
        elif n2 > n1:
            print(n2)
        else:
            print("os valores são iguais")
    elif ope == 4:
        n1 = int(input("digite um valor: "))
        n2 = int(input("digite outro valor: "))

    print("[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair de programa")
    ope = int(input("qual operação devo realizar?: "))







