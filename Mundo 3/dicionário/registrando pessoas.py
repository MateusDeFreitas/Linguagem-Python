pessoas  = []
idades   = []
mulheres = []
velhos   = []

while True:
    nome  = input("digite o nome da pessoa (ou '0' para parar): ")
    if nome == '0':
        break
    while True:
        sexo  = input(f"digite o genero de {nome}: ")
        if sexo in 'hH':
            idade = int(input(f"digite a idade do {nome}: "))
            break
        elif sexo in 'Mm':
            idade = int(input(f"digite a idade da {nome}: "))
            break
        else:
            print("ERRO!:, digite apenas M ou H")
    idades.append(idade)
    pessoa = {'nome':nome,'sexo':sexo,'idade':idade}
    pessoas.append(pessoa.copy())
    if pessoa['sexo'] in 'Mm':
        mulheres.append(pessoa.copy())
    pessoa.clear()

print("-="*40)
if len(pessoas) == 0:
    print("ninguém foi regitrado!")
elif len(pessoas) == 1:
    print("uma pessoa foi registrada!")
else:
    print("foram registradas",len(pessoas),"pessoas!")

print()
print("-="*40)
if len(pessoas) == 0:
    print("ninguém foi regitrado!")
elif len(pessoas) == 1:
    print("a média de idade registrada é",idades)
else:
    print("a média de idade do grupo registrado é:",sum(idades)/len(idades))

print()
print("-="*40)
if len(mulheres) == 0:
    print("nenhuma mulher foi regitrada!")
elif len(mulheres) == 1:
    print("uma mulher foi registrada, a",mulheres[0]['nome'])
else:
    print(len(mulheres), "mulheres foram registradas são elas:")
    cont = 0
    for mulher in mulheres:
        print(mulheres[cont]['nome'],end=', ')
        cont += 1

print()
print("-="*40)
cont2 = 0
for gente in pessoas:
    if gente['idade'] > sum(idades)/len(idades):
        velhos.append(gente)

if len(pessoas) == 2:
    print("a pessoa mais velha listada foi:",velhos)
elif len(pessoas) > 2:
    print("as pessoas acima da média de idade são")
    for velho in velhos:
        print(velhos[cont2]['nome'],end=', ')
        cont2 += 1
