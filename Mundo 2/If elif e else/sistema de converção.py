print("Escolha em qual formato será feita a converção\n [ 1 ] binário\n [ 2 ] octal\n [ 3 ] hexadecimal")


formato = input("digite o número equivalente ao formato desejado: ")
try:
    numero = int(input("digite um número: "))
    if formato == '1':
        print("o númro", numero, "convertido em binário é igual a", bin(numero))
    elif formato == '2':
        print("o númro", numero, "convertido em octal é igual a", oct(numero))
    elif formato == '3':
        print("o númro", numero, "convertido em hexadecimal é igual a", hex(numero))
    else:
        print("formato inexistente")
except:
    print("esse número não é converssível")





