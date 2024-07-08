registroJogador = {}
while True:
    numeroDePartidas = input('numero de partidas: ')
    if numeroDePartidas.isdigit():
        numeroDePartidas = int(numeroDePartidas)
        break
    else:
        print('numero de partidas invalido')
        continue

totalDeGols = 0
nome = ''
partida = 1

while True:
    nome = input('nome do jogador: ')
    if nome.replace(" ", "").isalpha():
        registroJogador['nome'] = nome
        break
    else:
        print('nome do jogador invalido')
        continue

golsPorPartida = []

for c in range(numeroDePartidas):
    while True:
        numeroDeGols = input('numero de gols: ')
        if numeroDeGols.isdigit():
            numeroDeGols = int(numeroDeGols)
            if numeroDeGols < 0:
                print('numero de gols invalido ')
                continue
            if numeroDeGols >= 0:
                golsPorPartida.append(f'na partida {partida} o jogador {nome} fez {numeroDeGols} gols')
                totalDeGols += numeroDeGols
                numeroDePartidas += 1
                break

registroJogador['gols'] = totalDeGols

print(registroJogador)

print(golsPorPartida)

print(f'a media de gols por partida foi {totalDeGols/len(golsPorPartida)}')
