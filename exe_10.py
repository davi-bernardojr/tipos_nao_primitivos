dict_for = {}
dict_while = {}
i = 0

for x in range(10) :
    dict_for[x] = x + 1

while i < 10 :
    dict_while[i] = i + 1
    i += 1
    
print(f"Dicionario iterado com for: {dict_for}")
print(f"Dicionario iterado com while: {dict_while}")