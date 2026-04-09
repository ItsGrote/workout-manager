
def isNumber(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Voce precisa digitar um numero para continuar.")



def validation(menuOption):
    while menuOption not in [1, 2, 3, 4, 5, 6]:
        print("Digite um numero valido para prosseguir !(1, 2, 3, 4, 5 ou 6)")
        
        menuOption = isNumber("")

    return menuOption



def yesNo(resposta):
    resposta = resposta.lower()

    while resposta not in ["s", "sim", "n", "nao"]:
        print("Responda com sim ou nao para prosseguir!")

        resposta = input()
    
    return resposta



def deleteValidation(delete, listaTreino):
    while delete  > len(listaTreino) or delete  <= 0:

        print(f"Nao existe treino na opcao {delete}")
        print(f"Digite um numero das opcoes a cima")

        delete = isNumber("")
    return delete



def emptyArray(lista):
    if (len(lista) == 0):
        return True
    return False