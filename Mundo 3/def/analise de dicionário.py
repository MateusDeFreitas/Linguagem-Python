def notas(*num, sit=False):
    lnotas = []
    for valor in num:
        lnotas.append(valor)
    dic = {"número de notas": len(lnotas),"maior nota":max(lnotas),"menor nota":min(lnotas),"média":sum(lnotas)/len(lnotas)}
    if sit == True:
        if dic['média'] <= 5:
            dic['situação'] = "Ruim"
        elif dic['média'] >= 7:
            dic['situação'] = "Boa"
        else:
            dic['situação'] = "Razoável"
    return dic


teste = notas(5,10,1,sit=True)
print(teste)
