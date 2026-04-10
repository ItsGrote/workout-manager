from workoutService import addWorkOut, getWorkOut, editWorkOut, deleteWorkOut
from utils import isNumber, yesNo, emptyArray, deleteValidation, validation
from menus import menuNoWorkOut, menuEdit, mainMenu

def handleAdd(listaTreino, diaTreino): 

    nomeTreino = input("Digite o nome do treino: ")

    listaExercicios = []

    while True:
        nome = input("Nome do exercicio: ")
        numSeries = isNumber("Numero de series: ")
        numRepeticoes = isNumber("Numero de repeticoes: ")
        totalCarga = isNumber("Carga usada em kg: ")

        addWorkOut(listaExercicios, nome, numSeries, numRepeticoes, totalCarga)


        print("Execicio salvo com sucesso!")
        print("Deseja adicionar mais exercicios para esse treino? Respoda com sim ou nao.")

        adicionarMais = yesNo(input())

        adicionarMais = adicionarMais.lower()
        if adicionarMais in ["s", "sim"]:
            continue
        else: 
            print(f"Aqui esta seu treino de {nomeTreino}:")
            print() 

            print(f"{nomeTreino.upper()}")

            for exercicio in listaExercicios:
                print(f"-> {exercicio['Exercicio']}")
                print(f"Series: {exercicio['Series']}")
                print(f"Repeticoes: {exercicio['Repeticoes']}")
                print(f"Carga: {exercicio['Carga']} kg")
                print()
                print()
                print("Ate o proximo treino!")
            break

    listaTreino.append({
        "Data" : diaTreino,
        "Nome do Treino" : nomeTreino,
        "Exercicios" : listaExercicios
    })

def handleViewWorkOut(listaTreino):
    if emptyArray(listaTreino):
        menuNoWorkOut()
        return 

    else:
        for treino in listaTreino:
            print(f"Data do treino: {treino['Data']}")
            print(f"Treino de {treino['Nome do Treino'].upper()}:")
            print("----------------")   

            for exercicio in treino["Exercicios"]:
                nomeExercicio = exercicio['Exercicio'].upper()
                print(f"-> {nomeExercicio}")
                print(f"Series: {exercicio['Series']}")                     
                print(f"Repeticoes: {exercicio['Repeticoes']}")
                print(f"Carga: {exercicio['Carga']}")
                print("-------------")

def handleEditWorkOut(listaTreino):

    if(emptyArray(listaTreino)):
            menuNoWorkOut()
            return
    else:
        while True:
            for index, treino in enumerate(listaTreino, start = 1):
                print(f"{index} - {treino['Nome do Treino']} ({treino['Data']})")
                    

                editarTreino = deleteValidation(isNumber("Digite o numero do treino que deseja editar? "), listaTreino) - 1

                treinoEscolhido = getWorkOut(listaTreino, editarTreino)


                for index, exercicios in enumerate(treinoEscolhido["Exercicios"], start = 1):
                    print(f"{index} - {exercicios['Exercicio']}") 
                
                editarExercicio = deleteValidation(isNumber("Numero do exercicio que deseja editar: "), treinoEscolhido["Exercicios"]) - 1

                print(f"Editando {listaTreino[editarTreino]['Nome do Treino']} ...")

                
                exercicioEscolhido = treinoEscolhido["Exercicios"][editarExercicio]



                while True:

                    menuEdit()

                    mapa = {
                        1 : "Exercicio",
                        2 : "Series",
                        3 : "Repeticoes",
                        4 : "Carga"
                    }

                    escolha = isNumber("Numero: ")

                    while escolha not in [1,2,3,4,5]:
                        print("Digite um numero dentro das opcoes para continuar (1, 2, 3, 4 ou 5)")
                        escolha = isNumber("Numero: ")


                    if escolha == 5:
                        print("Edicao encerrada!")
                        break
                    elif escolha == 1:
                        alteracao = input("Nome do exercicio: ")
                        editWorkOut(exercicioEscolhido, escolha, alteracao)
                        print(f"Nome do exercicio foi alterado para {alteracao} com sucesso!")
                    else:
                        alteracao = isNumber(f"Mudar {mapa[escolha]} para: ")
                        editWorkOut(exercicioEscolhido, escolha, alteracao)
                        print(f"Numero de {mapa[escolha].lower()} foi alterado para {alteracao} com sucesso!")

                    print("exercicio editado com sucesso!")

                    print("Deseja fazer outra alteracao nesse exercicio? Responda com sim ou nao.")
                    continuarEdicao = yesNo(input())

                    if continuarEdicao in ["n", "nao"]:
                        print("Edicao encerrada")
                        break


                print("Deseja alterar outro exercicio? Responda com sim ou nao")

                editarMais = yesNo(input())

                if editarMais in ["n", "nao"]:
                    print("Voltando para o menu...")
                    return
                
def handleDeleteWorkOut(listaTreino):
    if(emptyArray(listaTreino)):
        menuNoWorkOut()
        return
    else:
        for index, treino in enumerate(listaTreino, start = 1):
            print(f"{index} - {treino['Nome do Treino']} ({treino['Data']})")
                

        delete = isNumber("Digite o numero do treino que deseja deletar? ")
        delete = deleteValidation(delete, listaTreino) - 1
        
        deleteWorkOut(listaTreino, delete)

        print("Treino deletado com sucesso!")

def handleSelectWork(listaTreino):
    if(emptyArray(listaTreino)):
        menuNoWorkOut()
        return

        
    else:
        for index, treino in enumerate(listaTreino, start = 1):
            print(f"{index} - {treino['Nome do Treino']} ({treino['Data']})")
                

        verTreino = deleteValidation(isNumber("Digite o numero do treino que deseja ver? "), listaTreino) - 1


        escolha = getWorkOut(listaTreino, verTreino)


        print(f"{escolha['Nome do Treino'].upper()} ({escolha['Data']})")
        print("-------------")


        for exercicio in listaTreino[verTreino - 1]["Exercicios"]:
                nomeExercicio = exercicio['Exercicio'].upper()
                print(f"-> {nomeExercicio}")
                print(f"Series: {exercicio['Series']}")                     
                print(f"Repeticoes: {exercicio['Repeticoes']}")
                print(f"Carga: {exercicio['Carga']}")
                print("-------------")

def handleMenuOption():

    mainMenu()

    menuOption = isNumber("")

    validation(menuOption)

    return menuOption










