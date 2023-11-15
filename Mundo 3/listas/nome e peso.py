pessoas = []
pessoa  = []
pesos   = []
mais  = []
menos = []
cont = 0

while True:
    nome  = input("digite o nome (para parar digite '0'): ")
    if nome == '0':
        break
    peso = int(input("dite o peso dessa pessoa: "))
    cont += 1
    pessoa.append(nome)
    pessoa.append(peso)
    pessoas.append(pessoa[:])
    pesos.append(peso)
    if cont == 1:
        mais.append(pessoa[:])
    elif cont == 2:
        if peso > mais[-1][1]:
            mais.append(pessoa[:])
        else:
            mais.insert(0,pessoa[:])
    elif cont == 3:
        if peso > mais[-1][1]:
            mais.append(pessoa[:])
        elif peso > mais[-2][1]:
            mais.insert(1,pessoa[:])
        else:
            mais.insert(1,pessoa[:])
    else:
        if peso > mais[-1][1]:
            mais.append(pessoa[:])
            mais.remove(mais[0])
        elif peso > mais[-2][1]:
            mais.insert(2,pessoa[:])
            mais.remove(mais[0])
        elif peso > mais[-3][1]:
            mais.insert(1,pessoa[:])
            mais.remove(mais[0])
    if cont == 1:
        menos.append(pessoa[:])
    elif cont == 2:
        if peso < menos[-1][1]:
            menos.append(pessoa[:])
        else:
            menos.insert(0,pessoa[:])
    elif cont == 3:
        if peso < menos[-1][1]:
            menos.append(pessoa[:])
        elif peso < menos[-2][1]:
            menos.insert(1,pessoa[:])
        else:
            menos.insert(1,pessoa[:])
    else:
        if peso < menos[-1][1]:
            menos.append(pessoa[:])
            menos.remove(menos[0])
        elif peso < menos[-2][1]:
            menos.insert(2,pessoa[:])
            menos.remove(menos[0])
        elif peso < menos[-3][1]:
            menos.insert(1,pessoa[:])
            menos.remove(menos[0])
    pessoa.clear()
print("--"*40)
print("--"*40)
print(pessoas)
print("--"*40)
print("foram listadas",len(pessoas),"pessoas")
print("--"*40)
print("as pessoas mais pesadas listadas são:\n",
      mais[-1][0],"que possui",mais[-1][1],",\n",
      mais[-2][0],"que possui",mais[-2][1],"\ne",
      mais[-3][0],"que possui",mais[-3][1])
print("--"*40)
print("as pessoas mais pesadas listadas são:\n",
      menos[0][0],"que possui",menos[0][1],",\n",
      menos[1][0],"que possui",menos[1][1],"\ne",
      menos[2][0],"que possui",menos[2][1])