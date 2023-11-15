from time import sleep

def fatorial(n,show=False):
    """
    Esse cógigo fatora o primeiro parametro "n"
    e caso coloqiue o segundo parametro "show" como True
    a conta será explicada e o passo-a-passo será visivel
    """
    if show == True:
        print("-=-"*30)
        print(f"Fatoração é uma conta onde o número desejado ({n})\n é multiplicado pelo fator, que é igaual ao número ({n})\n subtraido por um até chegar a 0")
        print("-=-" * 30)
        sleep(5)
    mult = n - 1
    fator = n
    while True:
        if show == True:
            if mult == 1:
                print(f"{fator} multiplicado por {mult} continua sendo", fator * mult)
            else:
                print(f"{fator} multiplicado por {mult} é:",fator*mult)
            sleep(1)
        fator *= mult
        mult -= 1
        if mult == 0:
            break
    print("=="*30)
    if show == True:
        return f"Portanto fatoração do número {n} é {fator}"
    else:
        return f"O resultado da fatoração do número {n} é {fator}"


#help(fatorial)

#num = int(input("digite um número para fatorar"))
#print(fatorial(num))

print(fatorial(8))