larguraParedeMetros = float(input("quantos a largura da parede em metros? "))
alturaParedeMetros = (float(input("qual a altura da parede em metros? ")))

areaDaParede = alturaParedeMetros * larguraParedeMetros

metrosquadrados = alturaParedeMetros*larguraParedeMetros

litrosDetintaNecessarios = areaDaParede/2

print(f"para pintar a parede de {str(metrosquadrados)} metros quadrados são necessarios {litrosDetintaNecessarios} litros de tinta")
