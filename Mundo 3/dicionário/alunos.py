x = int(input("quantos alunos quer computar? "))
cont = 0

while x != cont:
    nome  = input("Digite o nome do aluno: ")
    media = float(input("Digite a média do aluno: "))
    situação = ''
    if media >= 6:
        situação = 'aprovado'
    else:
        situação = 'reprovado'
    cont += 1

    dados = {'nome':nome,'média':media,'situação':situação}
    print("-="*30)
    print("O nome do aluno é:",dados['nome'])
    print("A média do aluno é:",dados['média'])
    print("A situação do aluno é:",dados['situação'])
    print("-="*30)
    dados.clear()