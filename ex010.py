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

reaisNaCarteira = float(input("quantos reais voce tem na carteira "))

conversaoDolar = reaisNaCarteira/3

print(f"com {reaisNaCarteira} voce consegue comprar {conversaoDolar}")

print(f"com {cores['azul']}{reaisNaCarteira} reais na carteira {cores["magenta"]}voce consegue comprar {cores['verde']}{conversaoDolar:.2f} Dolares")