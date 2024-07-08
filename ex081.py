lista = []
while True:
    numero = input("Coloque um número: ")
    if numero.isdigit() or numero.isdecimal():
        numero = int(numero)
        lista.append(numero)
        continuar = input("Deseja continuar? (s/n) ")
        if continuar.lower() != 's':
            break
    else:
        print("Número inválido.")
        continue


lista_inteiros = [int(x) for x in lista]

print(len(lista))
print(sorted(lista , reverse=True))

contador_de_5 = 0
for c in lista:
    if c == 5:
        contador_de_5 += 1
print(f"existem {contador_de_5} numero 5 na lista")

