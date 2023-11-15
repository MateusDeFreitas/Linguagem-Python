from time import sleep

def contador(ini,fim,pas):
    print("-="*30)
    print(f"contagem de {ini} até {fim} com intervalos de {pas}: ")
    if fim < ini:
        for i in range(ini, fim-1, pas*-1):
            sleep(0.5)
            print(i, end=", ")
        print("FIM!")
    else:
        for i in range(ini,fim+1,pas):
            sleep(0.5)
            print(i,end=", ")
        print("FIM!")


a = int(input("Digite o início da contagem: "))
b = int(input("Digite o fim da contagem: "))
c = int(input("Digite o intervalo da contagem: "))

contador(a,b,c)
