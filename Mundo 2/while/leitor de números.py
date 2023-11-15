números = []

while not 999 in números:
    n = int(input("Digite um número: "))
    números.append(n)

print("você digitou",len(números),"números")
print("a soma desses números é",sum(números))