a = int(input("digite um número: "))
b = int(input("digite um número: "))
c = int(input("digite um número: "))
d = int(input("digite um número: "))

nuns = (a,b,c,d)
pares = []
for n in nuns:
    if n%2==0:
        pares.append(n)




print(nuns)

if 9 in nuns:
    print("o número nove apareceu",nuns.count(9),"vezes")
else:
    print("o número nove não foi digitado nenhuma vez")

if 3 in nuns:
    print("o número três está colocado na",nuns.index(3)+1,"posição")
else:
    print("o número três não foi digitado nenhuma vez")
print("nessa tupla há",len(pares),"números pares")
