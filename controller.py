from workoutService import getWorkOut, editWorkOut
from loadAndSave import save
def handleAdd(listaTreino, nomeTreino, diaTreino, listaEx): 

    listaTreino.append({
        "Data" : diaTreino,
        "Nome do Treino" : nomeTreino,
        "Exercicios" : listaEx
    })

    save(listaTreino)



def handleEditWorkOut(listaTreino, idxTreino, idxExercicio, opcao, alteracao):

    treinoEscolhido = getWorkOut(listaTreino, idxTreino)

    exercicioEscolhido = treinoEscolhido["Exercicios"][idxExercicio]

    editWorkOut(exercicioEscolhido, opcao, alteracao)

    save(listaTreino)


    
                
def handleDeleteWorkOut(listaTreino, idxTreino):
    listaTreino.pop(idxTreino)
    save(listaTreino)
    











