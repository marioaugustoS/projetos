salario = float(input("digite o seu salario "))

if round(salario,2) == salario:
    salario = True
else:
    salario = False

valorCasa = int(input("digite o valor da casa "))

tempoFinanciamento = int(input("em quantos meses voce vai pagar "))

if salario == True and valorCasa/tempoFinanciamento <= salario*0.3:
    print("financiamento aprovado")
elif salario == True and valorCasa/tempoFinanciamento >= salario*0.3:
    print("financiamento negado")
else:
    print("formato de salario invalido")