dados = {}

for i in range(1, 5):
    temp = {}  # Cria um dicionário temporário para cada iteração
    while True:
        nome = input("Qual é o seu nome? ")
        if nome.isalpha():
            temp['nome'] = nome
            break
        else:
            print("Nome inválido, insira novamente.")

    while True:
        sexo = input("Qual é o seu sexo? M ou F ")
        sexo_corrigido = sexo.lower()
        if sexo_corrigido in ['m', 'f']:
            temp['sexo'] = sexo_corrigido
            break
        else:
            print("Sexo inválido.")

    while True:
        idade = input("Coloque a sua idade: ")
        if idade.isdigit():
            idade = int(idade)
            if 5 <= idade <= 100:
                temp['idade'] = idade
                break
            else:
                print("A idade deve ser entre 5 e 100.")
        else:
            print("Idade inválida.")

    # Adiciona o dicionário temporário ao dicionário principal
    dados[f'dados_{i}'] = temp



print(dados)

homem_mais_velho = None
idade_homem_mais_velho = -1
mulheres_menos_de_20 = 0

for chave, valor in dados.items():
    # Verifica se a entrada é de um homem e atualiza os dados se ele for o mais velho até agora
    if 'sexo' in valor and valor['sexo'] == 'm':
        if 'idade' in valor and valor['idade'] > idade_homem_mais_velho:
            homem_mais_velho = valor['nome']
            idade_homem_mais_velho = valor['idade']

    # Conta mulheres com menos de 20 anos
    if 'sexo' in valor and valor['sexo'] == 'f':
        if 'idade' in valor and valor['idade'] < 20:
            mulheres_menos_de_20 += 1

# Imprime os resultados
print("Nome do homem mais velho:", homem_mais_velho)
print("Quantidade de mulheres com menos de 20 anos:", mulheres_menos_de_20)
print(dados)



"""
dados = {}

for _ in range(1,4):
    while True:
        nome =  input("qual é o seu nome ")
        if nome.isalpha() == True:
            dados[nome] = nome
            break

        elif nome.isalpha() == False:
            print("nome invalido insira novamente ")

    while True:
            sexo =  input("qual o seu sexo? M ou F ")
            if sexo.isalpha():
                sexoCorrigido = sexo.lower()
                if sexoCorrigido == "m" or  sexoCorrigido == "f":
                    dados['sexo'] = sexoCorrigido
                    break
                else:
                    print("sexo invalido ")
            else:
                print("sexo invalido")

    while True:
            idade = input("coloque a sua idade ")
            if idade.isdigit():
                idade = int(idade)

                if 5 <= idade <= 100:
                    dados['idade'] = idade
                    break
                else:
                     print("a idade deve ser entre 5 e 100  ")
            else:
                print("idade invalida")


print(dados) 
"""





