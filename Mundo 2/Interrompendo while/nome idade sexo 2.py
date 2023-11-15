pessoas         = []
homens          = []
pessoasmais18   = []
mulheres        = []
mulheresmenos20 = []

while True:
    p = {'nome':input("nome: "),'idade':int(input("idade: ")),'genero':input("genero: ")}
    pessoas.append(p)
    x = input("quer inscrever mais pessoas? [s/n]: ")
    if x == 'n':
        break

#----------------------------------------------------------------

for pessoa in pessoas:
    if pessoa['idade'] > 18:
        pessoasmais18.append(pessoa)

#----------------------------------------------------------------

for pessoa in pessoas:
    if pessoa['genero'] == 'h':
        homens.append(pessoa)
    else:
        mulheres.append(pessoa)

#----------------------------------------------------------------

for mulher in mulheres:
    if mulher['idade'] < 20:
        mulheresmenos20.append(mulher)

#----------------------------------------------------------------

print()

sub20m = len(mulheresmenos20)
print("a quantidade de mulheres nesse grupo com menos de 20 anos é",sub20m)

print()

maisde18 = len(pessoasmais18)
print("a quantidade de pessoas com mais de 18 anos no gropo é",maisde18)

print()

qnthomens = len(homens)
print("a quantidade de homens nesse grupo é",qnthomens)
