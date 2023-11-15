ter = int(input("digite o primeiro termo da PA: "))
raz = int(input("digite a razão da PA: "))
qnt = int(input("digite quantos termos terão a PA: "))

fim = 0
nqnt = 0
parar = 'x'
while not parar == "sim":
    qnt += nqnt
    while fim != qnt:
        print(ter)
        ter += raz
        fim += 1
    parar = input("quer parar? ")
    if parar != 'sim':
        nqnt = int(input("digite mais quantos termos terão a PA: "))
