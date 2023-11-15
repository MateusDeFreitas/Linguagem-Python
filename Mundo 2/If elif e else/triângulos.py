#para uma forma poder ser um triângulo
#cada um dos seus lados tem que ser menor do que a soma dos demais

l1 = float(input("digite o tamanho do lado 1: "))
l2 = float(input("digite o tamanho do lado 2: "))
l3 = float(input("digite o tamanho do lado 3: "))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print("esses segmentos possivelmente formam um triângulo.")

    if l1 == l2 == l3:
        print("se for o caso, esse é um triângulo equilátero")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("se for o caso, esse é um triângulo isósceles")
    else:
        print("se for o caso, esse é um triângulo escaleno")
else:
    print("esse segmentos não podem formar um triângulo.")


