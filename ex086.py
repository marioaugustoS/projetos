linha1 = []
linha2 = []
linha3 = []

for c in range(3):
    numero1 = input("coloque um numero ")
    if numero1.isdigit():
        numero1 = int(numero1)
        listaNumero = [numero1]
        linha1.append(listaNumero)

    else:
        print("insira um numero valido ")
        continue

for c in range(3):
    numero = input("coloque um numero ")
    if numero.isdigit():
        numero = int(numero)
        listaNumero = [numero]
        linha2.append(listaNumero)

    else:
        print("insira um numero valido ")
        continue

for c in range(3):
    numero = input("coloque um numero ")
    if numero.isdigit():
        numero = int(numero)
        listaNumero = [numero]
        linha3.append(listaNumero)

    else:
        print("insira um numero valido ")
        continue


print(linha1)
print(linha2)
print(linha3)

'''linha1 = []
linha2 = []
linha3 = []

novaLista1 = []
novaLista2 = []
novaLista3 = []

# Função para solicitar um número válido
def solicitar_numero():
    while True:
        entrada = input("coloque um numero: ")
        if entrada.isdigit():
            return int(entrada)
        else:
            print("Insira um número válido.")

# Preencher linha1
for c in range(3):
    numero1 = solicitar_numero()
    novaLista1.append([numero1])
    linha1.append(novaLista1[c])

# Preencher linha2
for c in range(3):
    numero2 = solicitar_numero()
    novaLista2.append([numero2])
    linha2.append(novaLista2[c])


# Preencher linha3
for c in range(3):
    numero3 = solicitar_numero()
    novaLista3.append([numero3])
    linha3.append(novaLista3[c])

print(linha1)
print(linha2)
print(linha3)

valorTotal = 0

for c in range(3):
    numeroLinha1 = linha1[c]
    valor = int(numeroLinha1[0])
    valorTotal += valor
    numeroLinha2 = linha2[c]
    valor = int(numeroLinha2[0])
    valorTotal += valor
    numeroLinha3 = linha3[c]
    valor = int(numeroLinha3[0])
    valorTotal += valor

valorTerceiraColuna = 0

for c in range(1):

    terceiroNumeroColuna1 = linha1[2]
    terceiroNumeroColuna2 = linha2[2]
    terceiroNumeroColuna3 = linha3[2]

    valor1 = int(terceiroNumeroColuna1[0])
    valor2 = int(terceiroNumeroColuna2[0])
    valor3 = int(terceiroNumeroColuna3[0])

    valorTerceiraColuna += valor1 + valor2 + valor3


maiorNumeroLinha2 = 0

primeiroNumeroLinha1 = linha2[0]
primeiroNumeroLinha2 = linha2[1]
primeiroNumeroLinha3 = linha2[2]

for c in range(2):
    maiorNumeroLinha2 = primeiroNumeroLinha1
    if maiorNumeroLinha2 < primeiroNumeroLinha2:
        maiorNumeroLinha2 = primeiroNumeroLinha2
        if maiorNumeroLinha2 < primeiroNumeroLinha3:
            maiorNumeroLinha2 = primeiroNumeroLinha3









print(f'o valor total foi de {valorTotal}')
print(f'a soma dos valores da terceira coluna é  {valorTerceiraColuna}')
print(f'o maior numero da segundo linha é {maiorNumeroLinha2[0]}')'''




