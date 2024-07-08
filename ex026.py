def contar_ocorrencias_caracteres(frase):
    contagem = {}
    for caractere in frase:
        if caractere in contagem:
            contagem[caractere] += 1
        else:
            contagem[caractere] = 1
    return contagem

frase = input("Digite uma frase: ")
ocorrencias = contar_ocorrencias_caracteres(frase)

print("Contagem de ocorrências de cada caractere:")
for caractere, quantidade in ocorrencias.items():
    print(f"O caractere '{caractere}' aparece {quantidade} vezes na frase.")
