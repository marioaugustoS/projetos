'''idade = int(input("coloque sua idade "))

tabelaIdade = {'mirim': (5, 9),
       'infantil': (10, 14),
       'junior': (15, 19),
       'senior': (20, 40),

       }



if idade in tabelaIdade['mirim']:
    print(f"[0;34m com {idade} voce é nadador mirim")'''

idade = int(input("coloque sua idade "))

if idade < 5:
    print("novo demais ")
elif idade >= 5 and idade < 9:
    print("nadador mirim")
elif idade >=9 and idade < 14:
    print("nadador infantil")
elif idade >=14 and idade <19:
    print("nadador junior")
elif idade >= 19 and idade <= 20:
    print("nadador senior")
elif idade > 20:
    print("nadador master")


