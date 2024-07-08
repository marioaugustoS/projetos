'''registroAluno = {}


def validar_nome(nome):
    if nome.isalpha():
        return True
    else:
        return False


def validar_nota(nota):
    try:
        nota = float(nota)
        return True
    except ValueError:
        return False

notas = []

for c in range(5):
    while True:
        nome = input('nome: ')
        if validar_nome(nome):
            registroAluno['nome'] = nome
            break
        else:
            print('nome invalido')
            continue
    for n in range(5):
        while True:

            nota = input('nota: ')
            if validar_nota(nota):
                notas.append(int(nota))
                media = sum(notas)/len(notas)
                registroAluno['media'] = media
                if media >= 7:
                    registroAluno['resultado'] = 'aprovado'
                else:
                    registroAluno['resultado'] = 'reprovado'
                notas = []
                break

print(registroAluno)'''

alunos = {}

# Solicitar informações sobre os alunos
quantidade_alunos = int(input("Quantos alunos deseja registrar? "))

for i in range(quantidade_alunos):
    nome_aluno = input("Digite o nome do aluno: ")
    notas_aluno = []
    for j in range(3):  # Supondo que serão inseridas 3 notas
        nota = float(input(f"Digite a nota {j+1} do aluno {nome_aluno}: "))
        notas_aluno.append(nota)
    alunos[nome_aluno] = {'notas': notas_aluno}

# Verificar se cada aluno foi aprovado ou não e adicionar essa informação ao dicionário
for aluno, info in alunos.items():
    media = sum(info['notas']) / len(info['notas'])
    if media >= 7:
        info['aprovado'] = True
    else:
        info['aprovado'] = False

# Exibir os resultados
for aluno, info in alunos.items():
    if info['aprovado']:
        print(f"{aluno} - Média: {sum(info['notas']) / len(info['notas']):.2f} - Aprovado")
    else:
        print(f"{aluno} - Média: {sum(info['notas']) / len(info['notas']):.2f} - Reprovado")
