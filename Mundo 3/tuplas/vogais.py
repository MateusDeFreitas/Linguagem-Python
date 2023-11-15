a = input('Digite uma palavra (sem acentos): ')
b = input('Digite uma palavra (sem acentos): ')
c = input('Digite uma palavra (sem acentos): ')

lista = (a,b,c)
vogais = []
cont = 0

for palavra in lista:
    for letra in palavra:
        if letra in "aeiou":
            cont += 1
            vogais.append(letra)
    print("a palavra '",palavra,"' tem",cont,"vogais, são elas:",vogais)
    vogais.clear()
    cont = 0
