somar = 1
multiplicar = 2
maior = 3
novosNumeros = 4
sairDoPrograma = 5


novo_valor1 = 0
novo_valor2 = 0
while True:
    valor1 = input("coloque o primeiro valor ")
    valor2 = input("coloque o segundo valor ")
    if valor1.isdigit() and valor2.isdigit():
        valor1 = int(valor1)
        valor2 = int(valor2)
        opção = input("escolha uma operação "
                      "1 - soma "
                      "2 - multiplicar "
                      "3 - maior numero "
                      "4 - novosNumeros "
                      "5 - Sair do programa ")
        if opção.isdigit() and 0 < int(opção) < 6:
            opção = int(opção)
            if int(opção) == 1:
                print(valor1 + valor2)
            elif int(opção) == 2:
                print(valor1*valor2)
            elif int(opção) == 3:
                if valor1 > valor2:
                    print(valor1)
                else:
                    print(valor2)
            elif int(opção) == 4:
                novo_valor1 = input("coloque um numero ")
                novo_valor2 = input("coloque um numero ")
                if novo_valor1.isdigit() and novo_valor2.isdigit():
                    novo_valor1 = int(valor1)
                    novo_valor2 = int(valor2)
            elif int(opção) == 5:
                print("voce encerrou o programa")
                break
            else:
                print("o numero deve ser de 1 a 5")
        elif 0 < opção < 6:
            print("o numero deve ser de 1 até 5")
    else:
        print("coloque um numero inteiro ")