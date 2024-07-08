tupla_palavras = ('casa', 'carro', 'cachorro', 'gato', 'sol', 'lua', 'árvore', 'banana', 'computador', 'livro')

vogais = ('a','e','i','o','u')

for palavra in tupla_palavras:
    vogais_encontradas = [letra for letra in palavra if letra in vogais]
    if vogais_encontradas:
        print(f"as vogais encontradas em {palavra} são {vogais_encontradas} ")