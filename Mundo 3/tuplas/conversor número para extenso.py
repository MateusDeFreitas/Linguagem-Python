n = int(input("digite um numero entre 0 e 20: "))
tup = ('zero','um','dois','três','quatro','cinco','seis','sete','oito',
    'nove','dez','onze','doze','treze','quatorze','quinze','dezesseis'
       ,'dezessete','dezoito','dezenove','vinte')

while True:
    if n < 0:
        break
    elif n not in range(0,21):
        n = int(input("digite um numero entre 0 e 20 ou um número negativo para parar: "))
    elif n in range(0,21):
        print(tup[n])
        n = int(input("digite um numero entre 0 e 20 ou um número negativo para parar: "))
