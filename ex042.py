lado1 = float(input("numero do primeiro lado  "))
lado2 = float(input("numero do segundo lado  "))
lado3 = float(input("numero do terceiro lado "))


if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 +lado3 > lado1:
    print('é possivel formar um triangulo')
    triangulo = True
else:
    print("não e possivel formar um triangulo")

if triangulo == True and lado1 ==  lado2 == lado3:
    print("o triangulo é equilatero")
if triangulo == True and (lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
    print("o triangulo é  isosceles")
if triangulo == True and lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print("o triangulo é escaleno")


"""

lado1 = float(input("Número do primeiro lado: "))
lado2 = float(input("Número do segundo lado: "))
lado3 = float(input("Número do terceiro lado: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print('É possível formar um triângulo')
    triangulo = True
else:
    print("Não é possível formar um triângulo")
    triangulo = False

if triangulo and lado1 == lado2 == lado3:
    print("O triângulo é equilátero")
if triangulo and (lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
    print("O triângulo é isósceles")
if triangulo and lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print("O triângulo é escaleno")
    """
