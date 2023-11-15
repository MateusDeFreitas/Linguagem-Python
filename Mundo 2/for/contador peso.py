qts = int(input("quantas pessoas serão analisadas: "))

y = 0
pesos = []

while y < qts:
    kg = int(input("digite um peso: "))
    pesos.append(kg)
    y += 1

maior = max(pesos)
menor = min(pesos)

print("o maior peso é:",maior)
print("o menor peso é:",menor)
