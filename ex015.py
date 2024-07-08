diasAlugados = int(input("dias alugados: "))
kmRodados = float(input("Kms Rodados: "))

valorTotal = (diasAlugados*100) + kmRodados*5

print(f"voce alugou o carro por {diasAlugados} dias e rodou {kmRodados} kilometros gerando um valor total de {valorTotal}R$")