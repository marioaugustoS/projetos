'''x = 1
numeroInicial = input("coloque um numero ")
razao = input("coloque o valor da razao ")
numeroRazoes = input("coloque o numero de razões ")
numeros = []
if numeroInicial.isdigit() and razao.isdigit():
    numeroInicial = int(numeroInicial)
    razao = int(razao)
    numeroRazoes = int(numeroRazoes)

else:
    print("numero invalido ")

while True:
    novoNumero = numeroInicial + ((x-1)*razao)
    x += 1
    numeros.append(novoNumero)
    if x == numeroRazoes:
        continuar = input("deseja continuar ")
        if continuar.isalpha():
            continuar.upper()
            if continuar.upper() == "S":
                continuação =  input("quantas razoes a mais? ")
                if continuação.isdigit():
                    int(continuação)
                    novoNumero = numeroInicial +((x-1)*int(continuação))
                    numeros.append(novoNumero)
            if continuar.upper() == "N":
                break'''





x = 1
numeroInicial = input("Coloque um número inicial: ")
razao = input("Coloque o valor da razão: ")
numeroRazoes = input("Coloque o número de razões: ")
numeros = []

if numeroInicial.isdigit() and razao.isdigit() and numeroRazoes.isdigit():
    numeroInicial = int(numeroInicial)
    razao = int(razao)
    numeroRazoes = int(numeroRazoes)
else:
    print("Número inválido.")

while True:
    novoNumero = numeroInicial + ((x - 1) * razao)
    numeros.append(novoNumero)
    x += 1
    if x > numeroRazoes:
        break

continuar = input("Deseja continuar? (S/N): ").upper()
if continuar == "S":
    continuação = input("Quantas razões a mais? ")
    if continuação.isdigit():
        continuação = int(continuação)
        for _ in range(continuação):
            novoNumero += razao
            numeros.append(novoNumero)

print(numeros)

