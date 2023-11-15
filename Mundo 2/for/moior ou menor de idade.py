qts = int(input("quantas pessoas serão analisadas: "))

y = 0
anos    = []
maiores  = []
menores = []

while y < qts:
    ano = int(input("qual seu ano de nascimento: "))
    anos.append(ano)
    y += 1

for ano in anos:
    if ano <= 2002:
        maiores.append(ano)
    else:
        menores.append(ano)

print("desse grupo",len(maiores),"pessoas são maiores de idade")
print("desse grupo",len(menores),"pessoas são menores de idade")


