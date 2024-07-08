import random

jogadaPc = random.randint(1,3)
jogadaPlayer = int(input("pedra 1 , papel 2, tesoura 3 "))

escolhaPlayer = ''
escolhaPc = ''


pedra = 1
papel = 2
tesoura = 3

while True:
    if jogadaPc < 1 or jogadaPc > 3:
        print("movimento invalido")
        break
    if jogadaPlayer < 1 or jogadaPlayer > 3:
        print("movimento invalido")
        break

    if jogadaPc == 1:
        escolhaPc = "pedra"
    if jogadaPc == 2:
        escolhaPc = "papel"
    if jogadaPc == 3:
        escolhaPc = "tesoura"
    if  jogadaPlayer == 1:
        escolhaPlayer = "pedra"
    if jogadaPlayer == 2:
        escolhaPlayer = "papel"
    if jogadaPlayer == 3:
        escolhaPlayer = "tesoura"

    if jogadaPc == jogadaPlayer:
        print("empate joguem denovo")
        jogadaPc = random.randint(1,3)
        jogadaPlayer = int(input("pedra 1 , papel2, tesoura3 "))


    elif jogadaPc == papel and jogadaPlayer == tesoura:
        print(f"o Pc escolheu {escolhaPc} e o player escolheu {escolhaPlayer} o player venceu")
        break
    elif jogadaPc == tesoura and jogadaPlayer == pedra:
        print(f"o Pc escolheu {escolhaPc} e o player escolheu {escolhaPlayer} o player venceu")
        break
    elif jogadaPc == pedra and jogadaPlayer == papel:
        print(f"o Pc escolheu {escolhaPc} e o player escolheu {escolhaPlayer} o player venceu")
        break

    else:
        print(f"o Pc escolheu {escolhaPc} e o player escolheu {escolhaPlayer} o Pc venceu")
        break

