def area(largura,comprimento):
    A = largura*comprimento
    print("=-" * 30)
    print("A largura do terreno é de:",largura,"metros")
    print("O comprimento do terreno é de:",comprimento,"metros")
    print()
    print("A área do terreno é:",A,"metros quadrados")
    print("=-" * 30)



lar = float(input("digite a largura do terreno(m): "))
com = float(input("digite o comprimento do terreno(m): "))
area(lar,com)