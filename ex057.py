c = 0
homens = 0
mulheres = 0
sexo = ''
while c < 10:
    sexo = input("Coloque seu sexo(M/F) ")
    if sexo.isalpha():
        sexo = sexo.upper()
        if sexo not in ["M", "F"]:
            print("Sexo inválido")
        elif sexo == "M":
            homens += 1
            c += 1
        elif sexo == "F":
            mulheres += 1
            c += 1
    if sexo.isalpha() == False:
        print("Resposta inválida")

print(f"Há um total de {homens} homens e {mulheres} mulheres.")
