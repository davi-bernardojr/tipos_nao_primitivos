informar = False
valores = {}
item = []
opcao = 0

def pesquisar(chave):
    achou = 0
    for i in valores:
        if (chave == i ):
            achou += 1
    if (achou > 0):
        return True
    else :
        return False
            
def insere_vlr(item):
    valores[item[0]] = item[1]

informar = True
while (informar == True):
    try :
        opcao = int(input("""0 - Sair
1 - Informar valores.
2 - Pesquisar chave.
3 - Exibir valores."""))
    except :
        print("Informe apenas numeros.")
    
    if (opcao > 3):
        print("Opcao invalida.")
    elif (opcao == 0 ):
        informar = False
    elif (opcao == 1 ):
        item.append(str(input("Informe a chave")))
        item.append(str(input("Informe o valor da chave")))
        if (pesquisar(item[0]) == True):
            print("O item não pode ser gravado pois a chave ja existe.")
        else :
            insere_vlr(item)
        item.clear()
    elif (opcao == 2 ):
        item.append(str(input("Informe a chave")))
        if (pesquisar(item[0]) == True):
            print(f"A chave {item[0]} existe.")
            print(f"Seu valor é {valores[item[0]]}.")
        else :
            print("A chave não existe.")
        item.clear()
    elif (opcao == 3 ):
        print(valores)
