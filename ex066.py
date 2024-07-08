numeros = []
while True:
    numero = input("coloque um numero ")
    if numero.isdigit():
        numero = int(numero)
        numeros.append(numero)
        if numero == 999:
            break


quantidade = len(numeros)
soma = sum(numeros)

print(numeros)
print(quantidade)
print(soma)