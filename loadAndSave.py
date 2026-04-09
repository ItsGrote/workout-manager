import json

def load():
 try:
    with open("treino.json", "r") as arquivo:
        return json.load(arquivo)
 except:
    return []


def save(listaTreino):
   with open("treino.json", "w") as arquivo:
      return json.dump(listaTreino, arquivo, indent = 4)