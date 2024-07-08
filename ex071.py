'''def verifica_valor(x):
    try:
        valor = int(x)
        if valor < 0:
            raise ValueError
        return valor
    except ValueError:
        print("Valor inválido. Insira um número inteiro positivo.")
        return None

def sacar_dinheiro(valor):
    cedulas = [50, 20, 10, 5, 1]
    contador_cedulas = [0] * len(cedulas)
    valor_original = valor

    for i, cedula in enumerate(cedulas):
        while valor >= cedula:
            valor -= cedula
            contador_cedulas[i] += 1

    return contador_cedulas, valor_original

valor_sacado = input("Quanto você deseja sacar? ")
valor_sacado = verifica_valor(valor_sacado)

if valor_sacado is not None:
    cedulas_quantidade, valor_sacado_original = sacar_dinheiro(valor_sacado)
    print(f"Você sacou um total de {valor_sacado_original} reais.")
    for quantidade, cedula in zip(cedulas_quantidade, [50, 20, 10, 5, 1]):
        print(f"{quantidade} nota(s) de {cedula} reais.")'''





valorSacado = input("quanto voce quer sacar ")
valorSacadoOriginal = valorSacado
def verificaValor(x):
    return int(x)

contadorCedula50 = 0
contadorCedula20 = 0
contadorCedula10 = 0
contadorCedula5 = 0
contadorCedula1 = 0

cedula50 =50
cedula20 =20
cedula10 =10
cedula5= 5
cedula1= 1



while valorSacado != 0:
    if verificaValor(valorSacado):
        valorSacado = int(valorSacado)
    if valorSacado - 50 >=0:
       valorSacado = valorSacado - cedula50
       contadorCedula50 += 1
    elif (valorSacado - cedula20) >= 0:
        valorSacado = valorSacado - cedula20
        contadorCedula20 +=1
    elif (valorSacado - cedula10) >= 0:
        valorSacado = valorSacado - cedula10
        contadorCedula10 +=1
    elif (valorSacado - cedula5) >= 0:
        valorSacado = valorSacado - cedula5
        contadorCedula5 +=1
    elif (valorSacado - cedula1) >=0:
        valorSacado = valorSacado - cedula1
        contadorCedula1 +=1

print(f"voce sacou um total de {valorSacadoOriginal} reais em {contadorCedula50} notas de 50, {contadorCedula20} de 20,{contadorCedula10} de 10, {contadorCedula5} de 5 e {contadorCedula1} de 1 real")
