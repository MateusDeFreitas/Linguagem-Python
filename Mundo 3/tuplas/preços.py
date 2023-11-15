prod = ("borracha",2,"lápiz",1,"caneta",4)

print('-'*40)
print(f'{"preços":^40}')
print('-'*40)

for p in range(0,len(prod)+1):
    if p%2==0:
        print(prod[p],".....................R$", end='')
    else:
        print(prod[p])


print('-'*40)