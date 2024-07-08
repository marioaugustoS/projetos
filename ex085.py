numeros = []
numerosPares = []
numerosImpares = []

for _ in range(7):
    while True:
        try:
            numero = int(input("Coloque um número: "))
            numeros.append(numero)
            break
        except ValueError:
            print("Por favor, insira apenas números.")

print("Lista de números:", numeros)

# Separar números pares e ímpares
for numero in numeros:
    if numero % 2 == 0:
        numerosPares.append(numero)
    else:
        numerosImpares.append(numero)

# Ordenar números pares e ímpares em ordem crescente
numerosPares.sort()
numerosImpares.sort()

# Criar lista corrigida
numerosCorrigidos = numerosPares + numerosImpares

print("Números corrigidos:", numerosCorrigidos)
