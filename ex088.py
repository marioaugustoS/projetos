import random

listaDejogos = [random.sample(range(1,61),6)for c in range (int(input("numero de jogos: ")))]

jogo = 1

for c in listaDejogos:
    print(f'jogo {jogo}:  {c}')
    jogo += 1

'''
import random
for x in range(int(input('Number of games: '))):
    print(f'Jogo {x+1}: {random.sample(range(1, 60), 6)}')

'''