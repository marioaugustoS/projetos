cores = {
    'RESET': '\033[0m',
    'BLACK': '\033[30m',
    'RED': '\033[31m',
    'GREEN': '\033[32m',
    'YELLOW': '\033[33m',
    'BLUE': '\033[34m',
    'MAGENTA': '\033[35m',
    'CYAN': '\033[36m',
    'WHITE': '\033[37m',
    'BOLD': '\033[1m',
    'UNDERLINE': '\033[4m',
}


lista_preçosEprodutos = ('leite' ,5 , 'agua',2, 'biscoito',7, 'farofa',9)

for c in range(0,len(lista_preçosEprodutos)):
    if c %2 == 0:
        print(f'{cores["BLUE"]}{lista_preçosEprodutos[c]} ---- {cores['RED']} {lista_preçosEprodutos[c+1]} R$')