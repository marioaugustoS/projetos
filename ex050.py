numeros = []
novoNumero = ''

for c in range(0, 6):
   while True:
        novoNumero = input("coloque um numero ")
        if novoNumero.isdigit():
            novoNumero = int(novoNumero)
            numeros.append(novoNumero)
            break

        else:
                print("numero invalido ")


for c in numeros:
    if c % 2 == 0:
        print(f"\033[0;35mo numero \033[0;31m {c} \033[0;32m é par")
