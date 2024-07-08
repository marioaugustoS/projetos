cores = {
    'roxo': '\033[0;35m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'azul': '\033[0;34m',
    'amarelo': '\033[0;33m',
    'ciano': '\033[0;36m',
    'magenta': '\033[0;35m',
    'branco': '\033[0;37m',
    'preto': '\033[0;30m'
}


n1 = float(input("escolha um numero: "))

dobro = n1*2
triplo = n1*3
raizQuadrada = n1**(1/2)

print(f"o dobro de {cores['vermelho']}{n1} é {cores['azul']}{dobro} o triplo é {triplo}{cores['amarelo']} e a raiz quadrada é {raizQuadrada}")