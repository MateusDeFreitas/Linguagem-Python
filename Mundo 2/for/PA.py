ter = int(input("digite o primeiro termo da PA: "))
raz = int(input("digite a razão da PA: "))
qnt = int(input("digite quantos termos terão a PA: "))
ult = raz*qnt+ter

for n in range(ter,ult,raz):
    print(n)
