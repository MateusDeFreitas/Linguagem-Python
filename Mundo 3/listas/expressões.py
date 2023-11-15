exp = input('digite uma expressão: ')

parenteses  = []
iparenteses = []
np = 0
ni = 0

for t in exp:
    if t == '(':
        parenteses.append(t)
        np += 1
    if t == ')' and np > ni:
        iparenteses.append(t)

if len(parenteses) != len(iparenteses):
    print("sua expressão está errada")
else:
    print("a expressão está correta")
