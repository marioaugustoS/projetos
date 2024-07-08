'''lista = [input("coloque um numero ") for c in range(1,6)]

listaNumeros = []
while len(listaNumeros) < 5:

       menorNumero = min(lista)
       listaNumeros.append(min(lista))
       lista.remove(menorNumero)

print(listaNumeros)'''

listaNumeros = []

while len(listaNumeros) < 5:
    numero = input("Digite um número: ")

    try:
        numero = float(numero)
        # Inserir o número na posição correta na lista
        if not listaNumeros or numero >= listaNumeros[-1]:
            listaNumeros.append(numero)
        else:
            for i in range(len(listaNumeros)):
                if numero <= listaNumeros[i]:
                    listaNumeros.insert(i, numero)
                    break
        print("Número inserido:", numero)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")

print("Lista ordenada:", listaNumeros)








