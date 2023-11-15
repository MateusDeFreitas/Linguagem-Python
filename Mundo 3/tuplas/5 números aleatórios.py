from random import randint

parar = ' '

while parar != 'parar':
    x = int(input("digite o número limite: "))
    a = randint(0,x)
    c = randint(0,x)
    b = randint(0,x)
    d = randint(0,x)
    e = randint(0,x)

    nums = (a,b,c,d,e)

    print("os números escolhidos foram:",nums)
    print("o maior número foi:",max(nums))
    print("o menor número foi:",min(nums))

    parar = input("digite 'parar' para enserrar o programa: ")