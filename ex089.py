'''registroAluno = [
    [
        input("Coloque seu nome: "),
        int(input("Primeira nota: ")),
        int(input("Segunda nota: "))
    ]
    for _ in range(int(input("Quantos alunos? ")))
]

for registro in registroAluno:
    print(f'aluno(a) {registro[0]} tirou nota {registro[1]} e {registro[2]} e teve media de {((int(registro[1] + int(registro[2]))/2))}')'''

registroAluno = [[input("Coloque seu nome: "), int(input("Primeira nota: ")), int(input("Segunda nota: "))] for _ in range(int(input("Quantos alunos? ")))]
for registro in registroAluno:
    print(f'aluno(a) {registro[0]} tirou nota {registro[1]} e {registro[2]} e teve media de {((int(registro[1] + int(registro[2]))/2))}')
