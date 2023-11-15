total = maisdemil = cont = menor = 0
barato = ''
while True:
    pruduto = input("dite o nome do produto: ")
    preço   = int(input("digite o preço desse produto: "))
    cont += 1
    total += preço
    if preço > 1000:
        maisdemil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = pruduto
    resp = ' '
    while resp not in 'SN':
        resp = str(input("quer continuar [S/N]?: ")).strip().upper()[0]
    if resp == 'N':
        break


print('{:-^40}'.format("fim do programa"))
print("o total gasto na compra foi",total,"reais")
print("no total",maisdemil,"produtos custaram mais de 1000 reais")
print("o produto mais barato foi",barato,"que custa",menor,"reais")