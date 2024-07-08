jogadores_brasileiros = (
    'Pelé',
    'Romário',
    'Ronaldo',
    'Rivaldo',
    'Ronaldinho Gaúcho',
    'Cafu',
    'Roberto Carlos',
    'Zico',
    'Sócrates',
    'Kaká',
    'Neymar',
    'Rivaldo',
    'Zico',
    'Tostão',
    'Jairzinho',
    'Rivellino',
    'Ronaldo Fenômeno',
    'Garrincha',
    'Rivaldo',
    'Kaká'
)
primeiros_colocados = (jogadores_brasileiros[0:5:1])
ultimos_colocados = (jogadores_brasileiros[len(jogadores_brasileiros):len(jogadores_brasileiros)-5:-1])
ordem_alfabetica = (sorted(jogadores_brasileiros))
posição_neymar = jogadores_brasileiros.index('Neymar')



print(primeiros_colocados)
print(ultimos_colocados)
print(ordem_alfabetica)

print(f'O jogador Neymar está na posição {posição_neymar + 1} na lista.')