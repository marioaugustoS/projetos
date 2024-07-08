'''
lado1 = int(input("primeiro lado do triangulo "))
lado2 = int(input("segundo lado do triangulo "))
lado3 = int(input("terceiro lado do triangulo "))


if lado1 - lado2 > 0 and lado1 -lado3 >0:
    maiorLado = lado1
if lado2 - lado1 > 0 and lado2 -lado3 >0:
    maiorLado = lado2
if lado3 - lado1 > 0 and lado3 -lado2 >0:
    maiorLado = lado3

if lado1 - lado2 < 0 and lado1 - lado3 < 0:
    menorLado = lado1
if lado2 - lado1 < 0 and lado2 - lado3 < 0:
    menorLado = lado2
if lado3 - lado1 < 0 and lado3 - lado2 < 0:
    menorLado = lado3

if menorLado == lado1 and maiorLado == lado3:
    ladoMedio = lado2

if menorLado == lado2 and maiorLado == lado3:
    ladoMedio = lado1

if menorLado == lado3 and maiorLado == lado1:
    ladoMedio = lado2

if menorLado == lado3 and maiorLado == lado2:
    ladoMedio = lado1

if menorLado == lado1 and maiorLado == lado2:
    ladoMedio = lado3

if menorLado == lado3 and maiorLado == lado1:
    ladoMedio = lado2

if menorLado + ladoMedio > maiorLado == True and menorLado + maiorLado > ladoMedio == True and ladoMedio + maiorLado == True:
    print("é possivel formar um triangulo")
else:
    print("não é possivel formar um triangulo")
'''

#forma correta

lado1 = int(input("primeiro lado do triangulo "))
lado2 = int(input("segundo lado do triangulo "))
lado3 = int(input("terceiro lado do triangulo "))

# Verifica se a soma de dois lados é maior que o terceiro para todos os lados
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("É possível formar um triângulo.")
else:
    print("Não é possível formar um triângulo.")
