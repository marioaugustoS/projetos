tabuada = [1,2,3,4,5,6,7,8,9,10]

while True:
    numero = input("coloque um numero ")
    if numero.isdigit():
        numero = int(numero)
        for x in tabuada:
            print(numero*tabuada[x-1])
            if numero == 999:
                break
