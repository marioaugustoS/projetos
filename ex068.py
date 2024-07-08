import random

def validar_par_ou_impar(escolha):
    return escolha.lower() == "par" or escolha.lower() == "ímpar"

tentativas = 0

while True:
    par_ou_impar = input("Par ou Ímpar? ").lower()
    if not validar_par_ou_impar(par_ou_impar):
        print("Escolha inválida. Por favor, escolha 'par' ou 'ímpar'.")
        continue

    jogada_pc = random.randint(1, 2)

    while True:
        numero_player = input("Escolha um número: ")
        try:
            numero_player = int(numero_player)
            break
        except ValueError:
            print("Número inválido. Por favor, insira um número inteiro.")

    resultado = jogada_pc + numero_player

    if (par_ou_impar == "par" and resultado % 2 == 0) or (par_ou_impar == "ímpar" and resultado % 2 != 0):
        print(f"O jogador venceu após {tentativas + 1} tentativas.")
        break

    tentativas += 1
