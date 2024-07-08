linha1 = []
linha2 = []
linha3 = []

novaLista1 = []
novaLista2 = []
novaLista3 = []

# Função para solicitar um número válido
def solicitar_numero():
    while True:
        entrada = input("coloque um numero: ")
        if entrada.isdigit():
            return int(entrada)
        else:
            print("Insira um número válido.")

# Preencher linha1
for c in range(3):
    numero1 = solicitar_numero()
    novaLista1.append([numero1])
    linha1.append(novaLista1[c])

# Preencher linha2
for c in range(3):
    numero2 = solicitar_numero()
    novaLista2.append([numero2])
    linha2.append(novaLista2[c])


# Preencher linha3
for c in range(3):
    numero3 = solicitar_numero()
    novaLista3.append([numero3])
    linha3.append(novaLista3[c])

print(linha1)
print(linha2)
print(linha3)

valorTotal = 0

for c in range(3):
    numeroLinha1 = linha1[c]
    valor = int(numeroLinha1[0])
    valorTotal += valor
    numeroLinha2 = linha2[c]
    valor = int(numeroLinha2[0])
    valorTotal += valor
    numeroLinha3 = linha3[c]
    valor = int(numeroLinha3[0])
    valorTotal += valor

valorTerceiraColuna = 0

for c in range(1):

    terceiroNumeroColuna1 = linha1[2]
    terceiroNumeroColuna2 = linha2[2]
    terceiroNumeroColuna3 = linha3[2]

    valor1 = int(terceiroNumeroColuna1[0])
    valor2 = int(terceiroNumeroColuna2[0])
    valor3 = int(terceiroNumeroColuna3[0])

    valorTerceiraColuna += valor1 + valor2 + valor3


maiorNumeroLinha2 = 0

primeiroNumeroLinha1 = linha2[0]
primeiroNumeroLinha2 = linha2[1]
primeiroNumeroLinha3 = linha2[2]

for c in range(2):
    maiorNumeroLinha2 = primeiroNumeroLinha1
    if maiorNumeroLinha2 < primeiroNumeroLinha2:
        maiorNumeroLinha2 = primeiroNumeroLinha2
        if maiorNumeroLinha2 < primeiroNumeroLinha3:
            maiorNumeroLinha2 = primeiroNumeroLinha3









print(f'o valor total foi de {valorTotal}')
print(f'a soma das 3 colunas foi de {valorTerceiraColuna}')
print(f'o maior numero da segundo linha é {maiorNumeroLinha2[0]}')


# Função para solicitar um número válido
'''def solicitar_numero():
    while True:
        entrada = input("coloque um numero: ")
        if entrada.isdigit():
            return int(entrada)
        else:
            print("Insira um número válido.")

# Função para preencher uma linha
def preencher_linha():
    linha = []
    for _ in range(3):
        numero = solicitar_numero()
        linha.append(numero)
    return linha

# Função para calcular a soma da terceira coluna
def calcular_soma_terceira_coluna(matriz):
    soma = 0
    for linha in matriz:
        soma += linha[2]
    return soma

# Preencher as linhas
linha1 = preencher_linha()
linha2 = preencher_linha()
linha3 = preencher_linha()

# Calcular a soma da terceira coluna
somaTerceiraColuna = calcular_soma_terceira_coluna([linha1, linha2, linha3])

# Encontrar o maior número da segunda linha
maiorNumeroLinha2 = max(linha2)

# Calcular o valor total
valorTotal = sum(sum(linha) for linha in [linha1, linha2, linha3])

print(f"O valor total foi de {valorTotal}")
print(f"A soma dos valores da terceira coluna foi de {somaTerceiraColuna}")
print(f"O maior número da segunda linha é {maiorNumeroLinha2}")


numero2 = solicitar_numero()
linha2.append(numero2)
valorTotal += numero2

numero3 = solicitar_numero()
linha3.append(numero3)
valorTotal += numero3

# Calcular a soma apenas dos valores da terceira coluna
somaTerceiraColuna = linha1[-1] + linha2[-1] + linha3[-1]

# Encontrar o maior número da segunda linha
maiorNumeroLinha2 = max(linha2)

print(f"O valor total foi de {valorTotal}")
print(f"A soma dos valores da terceira coluna foi de {somaTerceiraColuna}")
print(f"O maior número da segunda linha é {maiorNumeroLinha2}")

print(linha1[2])'''








