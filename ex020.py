import random

# Lista de alunos
alunos = ["Aluno1", "Aluno2", "Aluno3", "Aluno4"]

# Embaralhar a ordem dos alunos
random.shuffle(alunos)

# Imprimir a ordem dos alunos sorteados
print("A ordem dos alunos sorteados é:")
for aluno in alunos:
    print(aluno)
