import random

numero_aleatorio = random.randint(0,5)

palpite = int(input("de um palpite de 0 a 5 "))

if numero_aleatorio == palpite:
    print("parabens voce acertou")
elif numero_aleatorio != palpite:
    print(f"voce errou o numero era {numero_aleatorio}")