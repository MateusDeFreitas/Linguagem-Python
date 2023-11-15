def leiaint(msg):
    print("-"*30)
    while True:
        nu = input(msg)
        if nu.isnumeric():
            print("-" * 30)
            return nu
            break
        else:
            print("ERRO NÚMERO INVALIDO")




n = leiaint("digite um número: ")
print(f"Você digitou o número {n}")