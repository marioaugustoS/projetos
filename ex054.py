x = 2  # Defina o valor de x conforme necessário

dia = 23
mes = 4
ano = 2024

dadosNascimento = {}

for c in range(x):
    nome = input("Digite o seu nome: ")
    # Validar se o nome inserido contém apenas letras
    if nome.isalpha():
        # Solicitar o dia de nascimento até que uma entrada válida seja fornecida
        while True:
            diaNascimento = input("Digite o dia de nascimento: ")
            if diaNascimento.isdigit() and 1 <= int(diaNascimento) <= 31:
                diaNascimento = int(diaNascimento)
                print(f"Dia de nascimento: {diaNascimento}")
                break
            else:
                print("Entrada inválida para o dia de nascimento")

        # Solicitar o mês de nascimento até que uma entrada válida seja fornecida
        while True:
            mesNascimento = input("Digite o mês de nascimento: ")
            if mesNascimento.isdigit() and 1 <= int(mesNascimento) <= 12:
                mesNascimento = int(mesNascimento)
                print(f"Mês de nascimento: {mesNascimento}")
                break
            else:
                print("Entrada inválida para o mês de nascimento")

        # Solicitar o ano de nascimento até que uma entrada válida seja fornecida
        while True:
            anoNascimento = input("Digite o ano de nascimento: ")
            if anoNascimento.isdigit() and 1980 < int(anoNascimento) < 2020:
                anoNascimento = int(anoNascimento)
                print(f"Ano de nascimento: {anoNascimento}")
                break
            else:
                print("Entrada inválida para o ano de nascimento")

        # Adicionar os dados ao dicionário
        dadosNascimento[nome] = {'dia': diaNascimento, 'mes': mesNascimento, 'ano': anoNascimento}

print(dadosNascimento)


def verificaIdade(dadosNascimento):
    for nome, dados in dadosNascimento.items():
        ano = dados['ano']
        mes = dados['mes']
        dia = dados['dia']
        if ano < 2006 or (ano == 2006 and mes < 4) or (ano == 2006 and mes == 4 and dia < 23):
            print(f"{nome} é menor de idade")
        else:
            print(f"{nome} é maior de idade")


verificaIdade(dadosNascimento)

'''x = 2  # Defina o valor de x conforme necessário

dia = 23
mes = 4
ano = 2024


dadosNascimento = {}


for c in range(x):
    nome = str(input("Digite o seu nome: "))  # Corrigido o posicionamento do break

    diaNascimento = input("Digite o dia de nascimento: ")  # Input do dia de nascimento como string
    if diaNascimento.isdigit():
        diaNascimento = int(diaNascimento)  # Converta para inteiro se for um número
        if diaNascimento <= 31:
            print(f"Dia de nascimento: {diaNascimento}")
    else:
        print("Entrada inválida para o dia de nascimento")

    mesNascimento = input("mes nascimento ")
    if mesNascimento.isdigit():
        mesNascimento = int(mesNascimento)
        if mesNascimento <= 12:
            print(f"Mes do nascimento: {mesNascimento}")
        else:
            print("Mes invalido")
    anoNascimento = input("Digite o ano de nascimento:")
    if anoNascimento.isdigit():
        anoNascimento = int(anoNascimento)
        if anoNascimento > 1980 and anoNascimento < 2020:
            print(f"Ano do nascimento: {anoNascimento}")
        dadosNascimento[nome] = {'dia': diaNascimento,'mes': mesNascimento, 'ano': anoNascimento}

print(dadosNascimento)

def verificaIdade(dadosNascimento):
    for nome, dados in dadosNascimento.items():
        ano = dados['ano']
        mes = dados['mes']
        dia = dados['dia']
        if ano < 2006 or (ano == 2006 and mes < 4) or (ano == 2006 and mes == 4 and dia < 23):
            print(f"{nome} é menor de idade")
        else:
            print(f"{nome} é maior de idade")

verificaIdade(dadosNascimento)



def verificaIdade(dadosNascimento):
    if ano < 2006:
        print("menor de idade")
    elif ano == 2006 and mes < 4:
        print("menor de idade")
    elif ano == 2006 and mes == 4 and dia < 23:
        print("menor de idade")
    else:
        print("maior de idade")'''





