somador = 1
fim = 0
t = 0
n = int(input("digite quantos números terá a sequência: "))

print(t)
while not n == fim:
    print(t+somador)
    t += somador
    somador = t - somador
    fim += 1
