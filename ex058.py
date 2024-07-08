'''import random

numero_aleatorio = random.randint(0,5)

palpite = int(input("de um palpite de 0 a 5 "))

if numero_aleatorio == palpite:
    print("parabens voce acertou")
elif numero_aleatorio != palpite:
    print(f"voce errou o numero era {numero_aleatorio}")'''

import random

numeroAleatorio = random.randint(0,10)
palpite = ''
c = numeroAleatorio
tentativas = 0

while palpite != numeroAleatorio:
    palpite = input("coloque um numero de 0 a 10 ")
    if palpite.isdigit():
        palpite = int(palpite)
        if  0 < palpite > 9:
            print("palpite invalido coloque numeros de 0 a 10")
        else:
            tentativas += 1
    else:
        print("coloque um numero inteiro de 0 a 10 ")


if palpite == numeroAleatorio:
    print(f"voce acertou o numero com {tentativas} tentativas ")



