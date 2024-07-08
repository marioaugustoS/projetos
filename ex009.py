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



n1 = int(input("escolha um numero "))

Tabuada = [1,2,3,4,5,6,7,8,9]

resultados = []
strings = ["o primeiro é ","o segundo é ","o terceiro é ","o quarto é ","o quinto é ","o sexto é ","o sétimo é ","o oitavo é ","o nono é "]

for numero in Tabuada:
    resultado = n1*numero
    print(f'{cores['azul']}{strings[numero-1]}{cores['verde']}{resultado}')



