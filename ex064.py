numeros = []

while True:
    numero = input("coloque um numero ")
    if numero.isdigit():
        numero = int(numero)
        if numero == 999:
            break
        if numero != 999:
            numeros.append(numero)

print(sum(numeros))


