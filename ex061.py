x = 1
numeroInicial = input("coloque um numero ")
razao = input("coloque o valor da razao ")
numeros = []
if numeroInicial.isdigit() and razao.isdigit():
    numeroInicial = int(numeroInicial)
    razao = int(razao)

else:
    print("numero invalido")

while True:
    novoNumero = numeroInicial + ((x-1)*razao)
    x += 1
    numeros.append(novoNumero)
    if novoNumero > 10000:
        break

print(numeros)