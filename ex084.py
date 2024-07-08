pessoas = [['pedro',70],['maria',55],['joao',72],['sara',58]]




for pessoa in pessoas:
   pesos = [int(pessoa[1]) for pessoa in pessoas]
   peso_minimo = min(pesos)
   peso_maximo = max(pesos)

pessoa_mais_leve = [pessoa for pessoa in pessoas if pessoa[1] == peso_minimo]
pessoa_mais_pesada = [pessoa for pessoa in pessoas if pessoa[1] ==peso_maximo]




print(len(pessoas))
print(sorted(pesos))

print(f'pessoa mais leve {pessoa_mais_leve}')
print(f'pessoa mais pesada {pessoa_mais_pesada}')
