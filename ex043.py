peso = float(input("coloque o seu peso "))
altura = float(input("coloque sua altura em metros "))

if altura > 2.10:
    alturaCorrigida = altura/100
else:
    alturaCorrigida = altura

def calculaImc (peso,altura):
    return peso/(altura**2)

if calculaImc(peso,alturaCorrigida) < 18.5:
    print("abaixo do peso")
if calculaImc(peso,alturaCorrigida) >= 18.5 and calculaImc(peso,alturaCorrigida) <= 24.9:
    print("peso normal")
if calculaImc(peso,alturaCorrigida) > 24.9 and calculaImc(peso,alturaCorrigida) <= 29.9:
    print("sobrepeso")
if calculaImc(peso,alturaCorrigida) > 29.9:
    print("obesidade")

"""
peso = float(input("Coloque o seu peso (em kg): "))
altura = float(input("Coloque sua altura (em metros): "))

if altura > 2.10:
    alturaCorrigida = altura / 100
else:
    alturaCorrigida = altura

def calculaImc(peso, altura):
    return peso / (altura ** 2)

imc = calculaImc(peso, alturaCorrigida)

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc <= 24.9:
    print("Peso normal")
elif 25 <= imc <= 29.9:
    print("Sobrepeso")
else:
    print("Obesidade")
"""