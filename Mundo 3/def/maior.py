def maior(*num):
    valores = []
    print("Os valores listados são: ",end=' ')
    for valor in num:
        valores.append(valor)
        print(f'{valor}',end=', ')
    print()
    print("=-"*30)
    print("foram registrados",len(valores),"valores")
    print("dentre eles valores o maior é:",max(valores))
    valores.clear()



maior(10,20,30,40,50,60,70,80,90,100,101,22,13,77)


