registroGeral = {}

diaAtual = 1
mesAtual = 5
anoAtual = 2024

teste = []

def calculaidade(diaNascimento, mesNascimento, anoNascimento):
    if (mesNascimento < mesAtual) or (mesNascimento == mesAtual and diaNascimento <= diaAtual):
        idade = anoAtual - anoNascimento

    else:
        idade = anoAtual - anoNascimento - 1
    return idade


while True:
    quantidadePessoas = input('quantidade de pessoas: ')
    if quantidadePessoas.isdigit():
        quantidadePessoas = int(quantidadePessoas)
        break
    else:
        print('numero de pessoas invalido ')
        continue

for c in range(quantidadePessoas):
    while True:
        nome = input('nome: ')
        if nome.replace(" ", "").isalpha():
            nome = str(nome)
            break
        else:
            print('nome invalido')
            continue
    while True:
        carteiraDeTrabalho = input('carteira de trabalho (0 se inexistente)')
        if carteiraDeTrabalho.isdigit():
            carteiraDeTrabalho = int(carteiraDeTrabalho)
            break
        else:
            print('numero da carteira invalida')
            continue
    while True:
        idade = calculaidade(int(input('dia de nascimento')), int(input('mes de nascimento')), int(input('ano de nascimento')))
        if 1 < idade < 100 :
            idade = int(idade)
            break
        else:
            print('idade invalida')
    if carteiraDeTrabalho == 0:
        registroGeral[nome] = {'Carteira': carteiraDeTrabalho,'idade':idade}
        break
    if idade >= 18 and carteiraDeTrabalho != 0:
        while True:
            anoDeContratação = input('ano de contratação: ')
            if anoDeContratação.isdigit():
                anoDeAposentadoria = int(anoDeContratação) + 35
                break
            else:
                print('ano de contratação invalido')
                continue
    while True:
        salario = input('coloque seu salario: ')
        if salario.isdecimal():
            break
        else:
            print('salario invalido')
            continue
    registroGeral[nome] = {'Carteira': carteiraDeTrabalho, 'Idade': idade, 'AnoContratacao': anoDeContratação, 'AnoAposentadoria': anoDeAposentadoria, 'salario': salario}



    teste = [nome,carteiraDeTrabalho,idade,anoDeContratação,anoDeAposentadoria]



print(registroGeral)



print(teste)

