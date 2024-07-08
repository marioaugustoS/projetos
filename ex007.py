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



nome = input("coloque um nome: ")

nota1 = float(input('coloque a nota 1: '))
nota2 = float(input("coloque a nota 2: "))
nota3 = float(input("coloque a nota 3: "))

media = (nota1 + nota2 + nota3)/3

print(f"a media do aluno {cores['ciano']}{nome} é {cores['azul']}{round(media,1)}")