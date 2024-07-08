kmViagem = float(input("quantos km é a viagem "))

if kmViagem <= 200 :
    preçoViagem = kmViagem*0.5
    print(f"o valor da viagem foi de {preçoViagem:.2f}R$")
if kmViagem >200:
    preçoViagem = kmViagem*0.45
    print(f"o valor da viagem foi de {preçoViagem:.2f}R$")

