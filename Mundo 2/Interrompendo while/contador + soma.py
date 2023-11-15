n = s = 0
cont   = 0


while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    cont += 1
    s += n


print("você digitou",cont,"números")
print("a soma desses números é",s)