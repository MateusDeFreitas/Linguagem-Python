saque = int(input("digite quanto vc vai sacar?: "))

notasde50 = 0
notasde20 = 0
notasde10 = 0
notasde1 = 0


while True:
    if saque % 50 == 0 and saque > 0:
        saque -= 50
        notasde50 += 1
    elif saque % 20 == 0 and saque > 0:
        saque -= 20
        notasde20 += 1
    elif saque % 10 == 0 and saque > 0:
        saque -= 10
        notasde10 += 1
    elif saque % 1 == 0 and saque > 0:
        saque -= 1
        notasde1 += 1
    else:
        break



print("você recebeu",notasde50,"notas de 50,",notasde20,"notas de 20,",notasde10,"notas de 10 e",notasde1,"notas de 1 real")