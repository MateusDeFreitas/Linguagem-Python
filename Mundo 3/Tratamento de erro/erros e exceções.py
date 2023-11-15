def leiaInt(msg):
    while True:
        try:
            a = int(input(msg))
        except (ValueError):
            print("\033[31mERRO! digite um número real válido\033[m")
        else:
            return a
            break


def leiaFloat(msg):
    while True:
        try:
            b = float(input(msg))
        except:
            print("\033[31mERRO! digite um número real válido\033[m")
        else:
            return b
            break


a = leiaInt("digite um número inteiro: ")
b = leiaFloat("digite um número real: ")
print(f"você digitou o número inteiro {a} e o real {b}")