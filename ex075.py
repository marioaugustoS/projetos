tupla = tuple(int(input("coloque um numero ")) for c in range(1,5))

contador_de_noves = 0
numeros_pares = 0
primeiro_tres = 0
primeiro_tres = 0
for c in range(0,len(tupla)):
    if tupla[c] == 9:
        contador_de_noves += 1
    if tupla[c]% 2 == 0:
        numeros_pares +=1
    if tupla[c] == 3 and primeiro_tres < 1:
        print(f'o primeiro 3 esta na {c+1}a posição ')
        primeiro_tres +=1

print(contador_de_noves)
print(numeros_pares)






