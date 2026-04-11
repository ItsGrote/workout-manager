from utils import isNumber, yesNo, emptyArray, deleteValidation, validation
from workoutService import addWorkOut
from datetime import date
from menus import menuNoWorkOut, menuEdit, mainMenu

def collectWorkoutData():

    data = date.today()

    diaTreino = data.strftime("%d/%m/%Y")

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

        if adicionarMais in ["s", "sim"]:
            continue
        else: 
            break
    return nomeTreino, diaTreino, listaExercicios

def displayWorkout(nomeTreino, listaExercicios):
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


def selectWorkout(listaTreino):
    if(emptyArray(listaTreino)):
        menuNoWorkOut
        return None
    else:
        for index, treino in enumerate(listaTreino, start = 1):
            print(f"{index} - {treino['Nome do Treino']} {treino['Data']}")

        
        editarTreino = deleteValidation(isNumber("Digite o numero do treino que deseja: "), listaTreino) - 1
    
    return editarTreino
        
def selectExercise(treinoEscolhido):
    for index, exercicios in enumerate(treinoEscolhido["Exercicios"], start = 1):
        print(f"{index} - {exercicios['Exercicio']}") 
                
    editarExercicio = deleteValidation(isNumber("Numero do exercicio que deseja editar: "), treinoEscolhido["Exercicios"]) - 1
       
    return editarExercicio
    
def selectOption():

    menuEdit()

    escolha = isNumber("Numero: ")

    while escolha not in [1,2,3,4,5]:
        print("Digite um numero dentro das opcoes para continuar (1, 2, 3, 4 ou 5)")
        escolha = isNumber("Numero: ")

    return escolha
     
def collectNewValue(escolha):

        mapa = {
            1 : "Exercicio",
            2 : "Series",
            3 : "Repeticoes",
            4 : "Carga"
        }

        if escolha == 1:
            alteracao = input("Digite o nome do exercicio: ")
        elif escolha in [2,3,4]:
            alteracao = isNumber(f"Digite o novo numero de {mapa[escolha].lower()}: ")
        if escolha == 5:
            return None

        return alteracao

        


def deleteWorkoutData(listaTreino):
    
    if(emptyArray(listaTreino)):
        menuNoWorkOut()
        return None
    else:
        idxTreino = deleteValidation(isNumber("Digite o numero do treino a ser deletado: "), listaTreino) - 1
    return idxTreino


def displayHistory(listaTreino):
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
    return

def displayWorkoutOptions(listaTreino):
    if(emptyArray(listaTreino)):
        menuNoWorkOut()
        return
    
    for index, treino in enumerate(listaTreino, start = 1):
        print(f"{index} - {treino['Nome do Treino']} ({treino['Data']})")


def displayPastExcercise(listaTreino, idxTreino):


        print(f"{listaTreino[idxTreino]['Nome do Treino'].upper()} ({listaTreino[idxTreino]['Data']})")
        print("-------------")


        for exercicio in listaTreino[idxTreino]["Exercicios"]:
                nomeExercicio = exercicio['Exercicio'].upper()
                print(f"-> {nomeExercicio}")
                print(f"Series: {exercicio['Series']}")                     
                print(f"Repeticoes: {exercicio['Repeticoes']}")
                print(f"Carga: {exercicio['Carga']}")
                print("-------------")

def mainMenuOptions():
    mainMenu()

    menuOption = isNumber("")

    validation(menuOption)

    return menuOption
