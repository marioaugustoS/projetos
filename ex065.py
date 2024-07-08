numeros = []

while True:
    numero = input("coloque um numero ")
    if numero.isdigit():
        numero = int(numero)
        numeros.append(numero)
        continuar = input("deseja continuar? sim ou não? ")
        if continuar.lower() == "sim":
            ''
        if continuar.lower() == "nao":
            break

    elif not numero.isdigit():
        print("numero invalido" )

print(min(numeros))
print(max(numeros))

soma = sum(numeros)
media = soma/len(numeros)

print(f"a média dos numeros é {media}")