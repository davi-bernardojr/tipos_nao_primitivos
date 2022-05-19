lista = ['abc', 'xyz', 'aba', '1221', 'frt', 'jyt', 'ed']
maior = 0
pri_ult = 0

for i in lista:
    if (len(i) > 2):
        maior += 1
    if (i[0] == i[len(i)-1]):
        pri_ult += 1

print(f"Itens com mais que 2 elementos: {maior}")
print(f"Itens com a primeira e ultima letra iguais: {pri_ult}")