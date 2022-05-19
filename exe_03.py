lista = [1, 20, 3, 4, 5]
maior = 0

for i in range(len(lista)):
    if (maior < lista[i]):
        maior = lista[i]
    
print(maior)