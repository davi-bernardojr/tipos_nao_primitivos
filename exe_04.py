string = "google.com.br"
dicionario = {}
contain = ""

for i in string:
    if (len(dicionario) == 0):
        dicionario[i] = 0
    else:
        for x in dicionario:
            if (x != i):
                contain = i
        dicionario[i] = 0
    
for i in dicionario:
    for x in string:
        if (x == i):
            dicionario[i] += 1
            
print(dicionario)

