from datetime import date

def voto(ano_nasc):
    hj = date.today().year
    idade = hj - ano_nasc
    if idade >= 18 and idade < 65:
        return  f"com {idade} anos: Voto Obrigatório"
    elif idade >= 16 or idade >= 65:
        return f"com {idade} anos: Voto Opcional"
    else:
        return f"com {idade} anos: Voto Negado"

print("--"*30)
ano = int(input("Digite o ano do seu nascimento: "))
print(voto(ano))

