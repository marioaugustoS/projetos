frase = str(input("coloque sua frase "))

fraseSemEspaços = frase.replace(" ", "")
fraseCorrigida = fraseSemEspaços.lower()

if fraseCorrigida[::-1] == fraseCorrigida:
    print("é um palindromo")
else:
    print("nao e um palindromo")