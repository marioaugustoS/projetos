lista = [int(input("coloque um numero " ) ) for c in range(1,6) ]
print(lista)
print(min(lista))

print(max(lista))

menorNumero = min(lista)
maiorNumero = max(lista)


for p,v in enumerate(lista):

    if v == maiorNumero:
        print(f'o maior numero é {v} nas posições {p+1}')
    if v == menorNumero:
        print(f'o menor numero é {v} nas posições {p+1}')
