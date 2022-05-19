lista = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

for i in range(len(lista)):
    for x in range(len(lista)):
        if (lista[i][1] < lista[x][1]):
            lista[i], lista[x] = lista[x], lista[i]


print(lista)