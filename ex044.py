valorCompras = float(input("valor das compras "))
formaPagamento = int(input("forma de pagamento: 1 a vista, 2 parcelado "))


if formaPagamento == 1:
    formaPagamento2 = int(input("1 dinheiro,2 cartão "))
    if formaPagamento2 == 1:
         valorCompras = valorCompras*0.9
    elif formaPagamento2 == 2:
        valorCompras = valorCompras*0.95

elif formaPagamento == 2:
    parcelas = int(input("quantas parcelas? "))
    valorCompras = valorCompras*(1+parcelas/10)
else:
    print("opção invalida")

print(f"{valorCompras:.2f}")