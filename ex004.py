algo = input()

print('\033[0;34malgo é um digito\033[0;36m',algo.isdigit())
print('\033[0;34malgo é um espaço ? \033[0;36m',algo.isspace())
print('\033[0;34malgo é uma letra\033[0;36m? ',algo.isalpha())
print('\033[0;34malgo é uma letra ou numero? \033[0;36m',algo.isalnum())
print('\033[0;34malgo é letra maiuscula ? \033[0;36m',algo.isupper())
print('\033[0;34malgo é letra minuscula ? \033[0;36m',algo.islower())
