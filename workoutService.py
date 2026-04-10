from utils import isNumber, yesNo, deleteValidation
from loadAndSave import load, save


def addWorkOut(listaExercicios, nome, numSeries, numRepeticoes, totalCarga):

    exercicio = {
            "Exercicio" :  nome,
            "Series" : numSeries,
            "Repeticoes" : numRepeticoes,
            "Carga" : totalCarga
    }

    listaExercicios.append(exercicio)


    return listaExercicios



def getWorkOut(listaTreino, verTreino):


    treinoEscolhido = listaTreino[verTreino]

    return treinoEscolhido


    
def editWorkOut(exercicioEscolhido, campo, alteracao):
    
    exercicioEscolhido[campo] = alteracao

    return alteracao


    


def deleteWorkOut(listaTreino, delete):

    listaTreino.pop(delete)
    return listaTreino

        
