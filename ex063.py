'''numeroPosPosterior = 0
numeroPosterior = 0

numeroInicial = 1
numeroAnterior = 2

while True:
    numeroPosterior += numeroAnterior + numeroInicial
    numeroPosPosterior += numeroPosterior

    numeroInicial = numeroAnterior
    numeroAnterior = numeroPosterior
    numeroPosterior = numeroPosPosterior

    print(numeroAnterior)
    print(numeroPosterior)
    print(numeroPosPosterior)

    if numeroPosterior > 1000:
        break'''

numeroInicial = 0
numeroAnterior = 1

while True:
    print(numeroInicial)


    numeroPosterior = numeroInicial + numeroAnterior


    numeroInicial = numeroAnterior
    numeroAnterior = numeroPosterior

    if numeroPosterior > 1000:
        break


