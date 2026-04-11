
from loadAndSave import load
from controller import handleAdd, handleEditWorkOut, handleDeleteWorkOut
from UI import collectWorkoutData, displayWorkout, selectWorkout, selectExercise, selectOption, collectNewValue, deleteWorkoutData, displayHistory, displayWorkoutOptions, displayPastExcercise, mainMenuOptions



print("Bem-Vindo ao Gerenciador de Treinos!")
print()

listaTreino = load()

while(True):

    menuOption = mainMenuOptions()

    if menuOption == 1:
        nome, dia, listaEx = collectWorkoutData()

        handleAdd(listaTreino, nome, dia, listaEx)

        displayWorkout(nome, listaEx)
    
    elif menuOption == 2:
        displayHistory(listaTreino)

    elif menuOption == 3:
        displayWorkoutOptions(listaTreino)

        idx = selectWorkout(listaTreino)

        displayPastExcercise(listaTreino, idx)


    elif menuOption == 4:
        idxTreino = selectWorkout(listaTreino)

        if idxTreino == None:
            break
        
        treinoEscolhido = listaTreino[idxTreino]

        idxExercicio = selectExercise(treinoEscolhido)

        escolha = selectOption()

        if escolha == 5:
            print("voltando...")
            break

        alteracao = collectNewValue(escolha)

        handleEditWorkOut(listaTreino, idxTreino, idxExercicio, escolha, alteracao)
    elif menuOption == 5:
        displayWorkoutOptions(listaTreino)

        idxTreino = deleteWorkoutData(listaTreino)

        if idxTreino == None:
            break

        handleDeleteWorkOut(listaTreino, idxTreino)
    else:
        print("Ate a proxima!")
        break
    
        

