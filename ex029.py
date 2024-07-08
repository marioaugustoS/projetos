velocidade = float(input("velocidade do carro "))

valorMulta = (velocidade - 70)*7

if velocidade > 70:
    print(f"voce ultrapassou o limite de velocidade e foi multado em {valorMulta:.2f}R$")
else:
    print("voce esta dentro do limite de velocidade")
