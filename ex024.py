verificaNome = input("qual cidade voce nasceu ")

nomeCorrigido = verificaNome[:6].lower()

if nomeCorrigido[:5] == "santo":
    nomeCorrigido = True
    print("o nome da cidade começa com santo")

else:
    print("o nome da cidade não começa com santo")


print()






