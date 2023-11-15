def escreva(palavra):
    lista =[]
    for letra in palavra:
        lista.append(letra)
    nl = len(lista[:])+4
    print("="*nl)
    print(f'  {palavra}')
    print("="*nl)
    lista.clear()


escreva("HELO")
escreva("MATEUS")