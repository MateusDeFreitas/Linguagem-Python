nome    = input("Digite o nome: ")
ano     = int(input("Digite o ano de nascimento: "))
ctps    = input("Digite o número da carteira de trabalho(se não existir = 0): ")
contrat = ''
sal     = ''

if ctps != '0':
    contrat = int(input("Digite o ano da contratação: "))
    sal = int(input("Digite o salário: "))


trabalhador = {'nome':nome,'ano de nascimento':ano,'nº de CTPS':ctps,
               'ano de contratação':contrat,'salário':sal}

print("=-"*30)
print("O nome do indivíduo é",trabalhador['nome'])
print("A idade do indivíduo é",2023-trabalhador['ano de nascimento'])
if ctps != '0':
    print("O CPTS do indivíduo é",trabalhador['nº de CTPS'])
    print("O ano de contratação do indivíduo é", trabalhador['ano de contratação'])
    print("O salário do indivíduo é",trabalhador['salário'])
    print("O a aposentadoria do indivíduo será com",trabalhador['ano de contratação']+40-trabalhador['ano de nascimento'],"anos")
else:
    print("O indivíduo não trabalha")