tupla = (
    'Um',
    'Dois',
    'Três',
    'Quatro',
    'Cinco',
    'Seis',
    'Sete',
    'Oito',
    'Nove',
    'Dez',
    'Onze',
    'Doze',
    'Treze',
    'Quatorze',
    'Quinze',
    'Dezesseis',
    'Dezessete',
    'Dezoito',
    'Dezenove',
    'Vinte'
)

numero = input("escolha um numero de 1 a 20 ")

if numero.isdigit():
    numero = int(numero)


def verificanumero(x,numero):
    if  1 <=  numero <=20:
        print(x[(numero)-1])
        print(numero)
    else:
        print("numero invalido ")
verificanumero(tupla,numero)