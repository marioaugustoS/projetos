n1 = int(input("digite um numero "))

n2 = int(input("digite outro numero"))

def soma(a,b):
    return a+b

resultado = soma(n1,n2)

print('a soma de \033[0;35m{}'.format(n1), "e {}\033[0;34m".format(n2), 'é igual a {}'.format(resultado))


#int voce pede input de numeros inteiros e com float vc poe numeros decimais.