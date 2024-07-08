registroGeral = {}
mulheres = []

while True:
    numeroDePessoas = input('Quantas pessoas cadastradas: ')
    if numeroDePessoas.isdigit():
        numeroDePessoas = int(numeroDePessoas)
        break
    else:
        print('Número de pessoas inválido')

for c in range(numeroDePessoas):
    while True:
        nome = input('Qual o seu nome: ')
        if nome.replace(' ', '').isalpha():
            break
        else:
            print('Nome inválido')

    while True:
        idade = input('Qual a sua idade: ')
        if idade.isdigit():
            idade = int(idade)
            break
        else:
            print('Idade inválida')

    while True:
        sexo = input('Qual o seu sexo? M ou F: ')
        if sexo.upper() == 'M' or sexo.upper() == 'F':
            break
        else:
            print('Sexo inválido')

    registroGeral[nome] = {'idade': idade, 'sexo': sexo}
    if sexo.upper() == 'F':
        mulheres.append(registroGeral[nome])

print(f'{numeroDePessoas} pessoa(s) foram cadastradas')

somaIdadeMulheres = sum(mulher['idade'] for mulher in mulheres)

MediaIdadeDoGrupo = sum(pessoa['idade'] for pessoa in registroGeral.values())/numeroDePessoas

print(f'as mulheres do grupo são {mulheres}')

print(f'a média da idade do grupo é de {MediaIdadeDoGrupo} anos ')

idadeAcimaDaMedia = []

for pessoa in registroGeral.values():
    if pessoa['idade'] > MediaIdadeDoGrupo:
        idadeAcimaDaMedia.append(registroGeral[pessoa])
