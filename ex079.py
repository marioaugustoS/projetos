# Recebe o input do usuário
'''valores = [input("Digite um número: ") for c in range(1,6)]

# Tenta converter a entrada para float

for c in range(0,len(valores)):

    try:
        numero = float(valores[c])
        print("Número inserido:", numero)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
        continue

NumerosUnicos = []
for c,v in enumerate(valores):
    if v not in NumerosUnicos:
        NumerosUnicos.append(v)
    elif v in NumerosUnicos:
        print(f"o numero {v} é repetido")

listaOrdenada = sorted(NumerosUnicos)

maiorNumero = max(NumerosUnicos)
menorNumero = min(NumerosUnicos)

print(listaOrdenada)'''

NumerosUnicos = []
numeros_vistos = set()

while len(NumerosUnicos) < 5:
    valor = input("Digite um número: ")

    try:
        numero = float(valor)
        if numero in numeros_vistos:
            print(f"O número {numero} já foi inserido. Por favor, insira um número diferente.")
            continue
        NumerosUnicos.append(numero)
        numeros_vistos.add(numero)
        print("Número inserido:", numero)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")

if NumerosUnicos:
    listaOrdenada = sorted(NumerosUnicos)
    maiorNumero = max(NumerosUnicos)
    menorNumero = min(NumerosUnicos)

    print("Lista de números únicos:", listaOrdenada)
    print("Maior número:", maiorNumero)
    print("Menor número:", menorNumero)




