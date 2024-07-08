media = float(input("digite aqui sua media "))

def verificaNota(x):
    if x >= 7:
        print("aprovado")
    if x < 7 and x >= 5  :
        print("recuperação")
    if x < 5:
        print("reprovou")

(verificaNota(media))