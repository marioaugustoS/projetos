expressão = input('coloque a expressão ')

paranteseEsquerda = 0
parenteseDireita = 0

for c in expressão:
    if c == '(':
        paranteseEsquerda += 1
    if c == ')':
        parenteseDireita += 1


if parenteseDireita == paranteseEsquerda:
    print('a expressão esta correta ')
else:
    print("a expressão esta incorreta")

