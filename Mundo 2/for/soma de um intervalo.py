nu = int(input("numero de referência: "))
s = 0

for n in range(0,501,nu):
    if n % nu == 0:
        print(n, end=' ')
    s += n
print()
print("a soma dos multiplos é",s)