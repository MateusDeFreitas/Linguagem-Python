pessoa1 = {'nome':input("nome: "),'idade':int(input("idade: ")),'genero':input("genero: ")}
pessoa2 = {'nome':input("nome: "),'idade':int(input("idade: ")),'genero':input("genero: ")}
pessoa3 = {'nome':input("nome: "),'idade':int(input("idade: ")),'genero':input("genero: ")}
pessoa4 = {'nome':input("nome: "),'idade':int(input("idade: ")),'genero':input("genero: ")}

pessoas         = [pessoa1,pessoa4,pessoa3,pessoa2]
homens          = []
homensidade     = []
mulheres        = []
mulheresmenos20 = []

for pessoa in pessoas:
    if pessoa['genero'] == 'h':
        homens.append(pessoa)
    else:
        mulheres.append(pessoa)

for homem in homens:
    homensidade.append(homem['idade'])

print()

for homem in homens:
    if homem['idade'] == max(homensidade):
        print("o",homem['nome'],"é o mais velho dos homens")
    else:
        print("o",homem['nome'],"não é o mais velho dos homens")

print()

for mulher in mulheres:
    if mulher['idade'] < 20:
        mulheresmenos20.append(mulher)

print()

sub20m = len(mulheresmenos20)
print("a quantidade de mulheres nesse grupo com menos de 20 anos é",sub20m)



print()

idades = [pessoa1['idade'],pessoa2['idade'],pessoa3['idade'],pessoa4['idade']]
soma = sum(idades)
media = soma/4
print("a idade média do grupo é",media,"anos")