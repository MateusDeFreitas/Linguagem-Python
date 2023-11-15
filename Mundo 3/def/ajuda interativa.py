def ajuda(com):
    while True:
        print(help(com))
        com = input("digite uma função ou biblioteca: ")
        if com.upper() == "FIM":
            break

ajuda(print)