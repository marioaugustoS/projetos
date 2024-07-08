infoPeso = {}
nome = ''
peso = ''

for _ in range(1, 5):
    while True:
        nome = input("Coloque o seu nome: ")
        if nome.isalpha():
            break
        else:
            print("Nome inválido, tente novamente.")

    while True:
        peso = input("Coloque o seu peso: ")
        if peso.isdigit() and 0 < float(peso) < 250:
            peso = float(peso)
            infoPeso[nome] = peso
            break
        else:
            print("Peso inválido, tente novamente.")


print(infoPeso)

infoPesoOrganizado = sorted(infoPeso.items(), key=lambda x: x[1], reverse = False)

print(f"os pesos em ordem crescente são {infoPesoOrganizado}")

print(infoPesoOrganizado)