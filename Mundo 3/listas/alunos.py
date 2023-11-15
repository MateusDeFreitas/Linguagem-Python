Nome   = ' '
classe = []
aluno  = []

while True:
    nome = input("digite o nome ou 'parar' para encerrar o programa: ")
    if nome == 'parar':
        break
    nota1 = int(input("digite a primeira nota: "))
    nota2 = int(input("digite a segunda nota: "))
    media = (nota2+nota1)/2
    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    aluno.append(media)
    classe.append(aluno[:])
    aluno.clear()

for alun in classe:
    print('-' * 15)
    print(alun)
print("-+"*20)

vontade = ' '
while vontade != 'parar':
    vontade = input("digite o nome do aluno que deseja verificar ou 'parar' para encerrar o programa: ")
    for alun in classe:
        if vontade == alun[0]:
            print("O aluno é:",alun[0])
            print("Sua primeira nota é:",alun[1])
            print("Sua segunda nota é:",alun[2])
            print("Sua média é:", alun[3])
            print("-+"*20)