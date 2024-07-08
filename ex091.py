'''import random

resultados = {}

for c in range(4):
    while True:
        nome = input('nome do jogador: ')
        if nome.isalpha():
            numeroSorteado = random.randint(1, 6)
            resultados[nome] = numeroSorteado
            break
        else:
            print('nome invalido')
            continue

valorMaisAlto = max(resultados.keys())

vencedoresSorteio = resultados[valorMaisAlto]

print("Os vencedores do sorteio com o número", valorMaisAlto, "são:", vencedoresSorteio)

print(resultados)'''

import random

def realizar_sorteio():
    resultados = {}

    for c in range(4):
        while True:
            nome = input('Nome do jogador: ')
            if nome.isalpha():
                numeroSorteado = random.randint(1, 6)
                if numeroSorteado not in resultados:
                    resultados[numeroSorteado] = [nome]
                else:
                    resultados[numeroSorteado].append(nome)
                break
            else:
                print('Nome inválido')
                continue

    return resultados

while True:
    # Realizar o sorteio
    resultados = realizar_sorteio()

    # Encontrar o valor máximo sorteado
    maximo = max(resultados.keys())

    # Verificar se há empate
    if len(resultados[maximo]) > 1:
        print("Empate! Novo sorteio será realizado.")
    else:
        # Se não houver empate, encontramos o vencedor
        vencedor = resultados[maximo][0]
        print("O vencedor do sorteio com o número", maximo, "é:", vencedor)
        break



