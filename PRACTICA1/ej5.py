import random
from queue import LifoQueue

def generaCadena(num_elementos):
    lista = [0] * num_elementos
    for i in range(num_elementos):
        if(random.randint(0, 1)):
            lista[i]="]"
        else:
            lista[i]="["

    return lista

def checkCadena(lista):
    p=LifoQueue()
    correcto = True
    i = 0
    while i < len(lista) and correcto:
        simbolo = lista[i]
        if simbolo == "[":
            p.put(simbolo)
        else:
            if p.empty():
                correcto = False
            else:
                p.get()
        i = i + 1

    if correcto and p.empty():
        return True
    else:
        return False

