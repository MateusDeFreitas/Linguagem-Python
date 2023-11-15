n = int(input("digite um número: "))
mult = 0
for i in range(2,n):
    if (n%i==0):
        print(n,"é divisivel por",i)
        mult += 1
if (mult == 0):
    print("esse número é primo")
else:
    print("esse número não é primo")
    print(n,"é multiplo de",mult,"números")



