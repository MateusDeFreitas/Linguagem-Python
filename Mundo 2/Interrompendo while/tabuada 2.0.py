while True:
    num    = int(input("digite o número da tabuada desejada: "))
    if num < 0:
        break
    print("--------------------------------------")
    for m in range(0,11):
        print(num,"vezes",m,"é igual a",m*num)
    print("--------------------------------------")
