lista = [10, 100, 30, 20, 10, 20]
aux = []

print(lista)

for i in lista:
    if i not in aux:
        aux.append(i)

aux.sort()  
print(aux)