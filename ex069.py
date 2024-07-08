def validar_sexo(x):
    return x.lower() == "f" or x.lower() == "m"


def validar_idade(x):
    return x.isdigit()


pessoas = []

while True:
    sexo = input("Qual é o seu sexo (f/m)? ").lower()
    idade = input("Coloque sua idade: ")

    if not validar_sexo(sexo) and not validar_idade(idade):
        print("Sexo e idade inválidos.")
        continue
    elif not validar_sexo(sexo):
        print("Sexo inválido.")
        continue
    elif not validar_idade(idade):
        print("Idade inválida.")
        continue

    pessoa = {'sexo': sexo, 'idade': idade}
    pessoas.append(pessoa)

    while True:
        continuar = input("Deseja adicionar outra pessoa? (s/n): ").lower()
        if continuar == 's':
            break
        elif continuar == 'n':
            break
        else:
            print("Opção inválida. Por favor, escolha 's' para sim ou 'n' para não.")

    if continuar != 's':
        break

print("Lista de pessoas:")
for x, y in enumerate(pessoas, start=1):
    print(f"Pessoa {x} - Sexo: {y['sexo']} - Idade: {y['idade']}")

total_homens = sum(1 for y in pessoas if y['sexo'] == 'm')
total_adultos = sum(1 for pessoa in pessoas if int(pessoa['idade']) > 18)
mulheres_jovens = sum(1 for pessoa in pessoas if int(pessoa['idade']) > 18 and pessoa['sexo'] == 'f')

print(f'{total_adultos} adultos ')
print(f'{total_homens} homens')
print(f'{mulheres_jovens} mulheres jovens ')
