def metade(n,m=False):
    r = n/2
    if m == False:
        return r
    else:
        return moeda(r)

def dobro(n,m=False):
    r = n*2
    if m == False:
        return r
    else:
        return moeda(r)

def aumento(v,a,t=1,m=False):
    if t == 1:
        r = v * (1+(a/100))
    elif t == 2:
        r = v + a
    if m == False:
        return r
    else:
        return moeda(r)

def redução(v,a,t=1,m=False):
    if t == 1:
        r = v * (1-(a/100))
    elif t == 2:
        r = v - a
    if m == False:
        return r
    else:
        return moeda(r)

def moeda(n):
    m = str(n)
    return m+"R$"

def resumo(p,a,r,f=True):
    if f == True:
        print("-="*15)
        print(" "*12,"RESUMO")
        print("-=" * 15)
        print("o valor analisado é",moeda(p))
        print(f"a metade de {moeda(p)} é {metade(p, True)}")
        print(f"o dobro de {moeda(p)} é {dobro(p, True)}")
        print(f"aumentando {moeda(p)} em {a}%, temos {aumento(p, a, m=True)}")
        print(f"reduzindo {moeda(p)} em {r}%, temos {redução(p, r, m=True)}")
    else:
        print("-=" * 15)
        print(" " * 12, "RESUMO")
        print("-=" * 15)
        print("o valor analisado é",p)
        print(f"a metade de {p} é {metade(p)}")
        print(f"o dobro de {p} é {dobro(p)}")
        print(f"aumentando {p} em {a}%, temos {aumento(p, a)}")
        print(f"reduzindo {p} em {r}%, temos {redução(p, r)}")
