from datetime import date
from loadAndSave import load, save
from controller import handleAdd, handleViewWorkOut, handleEditWorkOut, handleDeleteWorkOut, handleSelectWork, handleMenuOption



print("Bem-Vindo ao Gerenciador de Treinos!")
print()

listaTreino = load()

while(True):

    data = date.today()
    diaTreino = data.strftime("%d/%m/%Y")

    action = {
        1 : lambda : handleAdd(listaTreino, diaTreino),
        2 : lambda : handleViewWorkOut(listaTreino),
        3 : lambda : handleSelectWork(listaTreino),
        4 : lambda : handleEditWorkOut(listaTreino),
        5 : lambda : handleDeleteWorkOut(listaTreino)
    }


    menuOption = handleMenuOption()

    if menuOption == 6:
        print("Ate a proxima!")
        break

    action[menuOption]()

    if menuOption in [1,4,5]:
        save(listaTreino)
        

