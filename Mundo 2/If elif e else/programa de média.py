nnotas = int(input("digite quantas notas irâo compor a média: "))
notas = []

while len(notas) < nnotas:
    nota = float(input("digite a nota: "))
    notas.append(nota)

soma = sum(notas)
divisor = len(notas)

media = soma/divisor
print("A média das notas é:",media)

if media < 5:
    print("Este aluno está reprovado")
elif media >= 7:
    print("Este aluno está aprovado")
else:
    print("Este aluno está em recuperação")