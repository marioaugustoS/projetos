x = 10
numero = int(input("coloque o numero inicial "))
razao = int(input("coloque a razao da p.a "))

numeros = []

for c in range(x):
    while True:
        novoNumero = numero + (c*razao)

        numeros.append(novoNumero)
        print(novoNumero)
        break

    if novoNumero > 1000:
        break

print(numeros)