import time

num    = int(input("digite o número da tabuada desejada: "))
limite = int(input("digite até qual multiplicador a tabuada deve ir: "))
inter  = float(input("digite o intervalo de tempo desejado: "))

for m in range(0,limite):
    print(num,"vezes",m,"é igual a",m*num)
    time.sleep(inter)