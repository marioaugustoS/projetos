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


n1 = int(input("escolha um numero: "))

antecessor = n1 -1
sucessor = n1+1

print (f"o antecessor de \033[0;36m{n1} é {antecessor} e o sucessor é 'vermelho' {sucessor}")

print(f"O antecessor de {cores['ciano']}{n1}\033[0m é {antecessor} e o sucessor é {cores['vermelho']}sei la {sucessor}")