anoAtual = 2024
mesAtual = 8
diaAtual = 22

diaNascimento = int(input("dia de nascimento "))
mesNascimento = int(input("mes de nascimento "))
anoNascimento = int(input("ano de nascimento "))

if anoAtual - anoNascimento < 18:
    print("ainda não precisa se alistar")
elif anoAtual - anoNascimento == 18 and mesAtual > mesNascimento and diaAtual > diaNascimento:
    print("daqui a pouco voce tem que se alistar")
elif anoAtual - anoNascimento ==18 and mesAtual < mesNascimento and diaAtual < diaNascimento:
    print("voce tem até os 19 anos para se alistar")
elif anoAtual - anoNascimento ==18 and mesAtual == mesNascimento and diaAtual > diaNascimento:
    print("daqui a alguns dias voce pode se alistar")
elif anoAtual - anoNascimento ==18 and mesAtual == mesNascimento and diaAtual < diaNascimento:
    print("voce fez 18 esse mes e pode se alistar")
elif anoAtual - anoNascimento ==18 and mesAtual == mesNascimento and diaAtual == diaNascimento:
    print("feliz aniversario , bora se alistar? ")
elif anoAtual - anoNascimento > 18 :
    print("o prazo de alistamento ja passou")