fr = input("uma frase: ")

normal  = fr
reverso = fr[::-1]

lnormal  = []
lreverso = []

print(normal)
print(reverso)
print()
for i in normal:
    if i != " ":
     lnormal.append(i)
for l in reverso:
    if l != " ":
        lreverso.append(l)

print(lnormal)
print(lreverso)
print()

if lnormal == lreverso:
    print("essa frase é um polindromo")
else:
    print("essa é uma frase comum")
