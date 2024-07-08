catetoOposto = int(input("comprimento do cateto oposto: "))
catetoAdjacente = int(input("coloque o comprimento do cateto adjacente: "))

quadradoHipotenusa = catetoOposto**2 + catetoAdjacente**2

hipotenusa = quadradoHipotenusa**(1/2)

print(f"o valor dos catetos são {catetoAdjacente} e {catetoOposto} e a hipotenusa é {hipotenusa:.}")