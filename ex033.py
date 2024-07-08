n1 = float(input("coloque um numero "))
n2 = float(input("coloque um numero "))
n3 = float(input("coloque um numero "))



if n1 - n2 > 0 and n1-n3 >0:
    print(f"{n1} é o maior numero")
elif n2 - n1 >0 and n2 -n3 >0:
    print(f"{n2} é o maior numero")
elif n3 - n2 > 0 and n3-n1 >0:
    print(f"{n3} é o maior numero")

if n1 - n2 == 0 :
    print(f"o numero {n1} e {n2} são iguais")
if n2 - n3 == 0:
    print(f"os numeros {n2} e {n3} são iguais")
if n1 - n3 == 0:
    print(f"os numeros {n1} e {n3} são iguais")


if n1 - n2 < 0 and n1-n3 <0:
    print(f"{n1} é o menor numero")
elif  n2 - n1 < 0 and n2-n3 <0:
    print(f"{n2} é o menor numero")
elif  n3 - n1 < 0 and n3-n2 <0:
    print(f"{n3} é o menor numero")