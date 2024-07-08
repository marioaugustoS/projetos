numero = ''
resultado = 1
while True:
    numeroInicial = input("Coloque um número inteiro positivo: ")
    if numeroInicial.isdigit():
        numeroInicial = int(numeroInicial)
        if numeroInicial > 0:
            numero = numeroInicial
            numero = int(numero)
            for x in range(1, numero):
                resultado *= x
            break
        else:
            print("Por favor, coloque um número inteiro positivo.")
    else:
        print("Por favor, coloque um número inteiro positivo.")

print(f"O fatorial de {numeroInicial} é {resultado}")
