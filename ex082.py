lista = []

while True:
    numero = input("coloque um numero")
    if numero.isdigit() or numero.isdecimal():
        numero = float(numero)
        lista.append(numero)
        continuar = input("deseja continuar ? sim/nao")
        if continuar.lower() == 'sim':
            continue
        if continuar.lower() == 'nao':
            break
        else:
            print("sim ou nao?")
            continue
    else:
        print("numero invalido ")
        continue

listaPares = []
listaImpares = []

for c in lista:
    if c % 2 == 0:
        listaPares.append(c)
    if c % 2 != 0:
        listaImpares.append(c)

print(lista)
print(listaPares)
print(listaImpares)
