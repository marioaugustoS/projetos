'''import random
lista_numeros = ()
for c in range(0,5):
    numero_aleatorio = random.randint(1,100)
    lista_numeros.append(numero_aleatorio)'''

import random
#lista_numeros = (random.randint(1,100,),random.randint(1,100,),random.randint(1,100,),random.randint(1,100),random.randint(1,100))

lista_numeros =  tuple(random.randint(1, 10) for  c in range(1,6))
print(lista_numeros)
print(max(lista_numeros))
print(min(lista_numeros))

#from random import randint
#a = tuple(randint(1, 5) for i in range(5))

#print(f'Os números sorteados foram {a}, o maior é {max(a)} e o menor é {min(a)}.')
#
#