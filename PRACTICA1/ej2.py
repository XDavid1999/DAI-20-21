import random
from time import time

def ordenaAleatorio(num_elementos):
    lista = [0] * num_elementos
    for i in range(num_elementos):
        lista[i] = random.randint(0, num_elementos)
      
    tini_burbuja = time() 
    lista = ordenacionBurbuja(lista)
    tfin_burbuja = time() 
    t_burbuja = tfin_burbuja - tini_burbuja
    
    tini_seleccion = time() 
    lista = ordenacionSeleccion(lista)
    tfin_seleccion = time() 
    t_seleccion = tfin_seleccion - tini_seleccion

    tini_mezcla = time() 
    lista = ordenamientoPorMezcla(lista)
    tfin_mezcla = time() 
    t_mezcla = tfin_mezcla - tini_mezcla

    tini_insercion = time() 
    lista = ordenacionInsercion(lista)
    tfin_insercion = time() 
    t_insercion = tfin_insercion - tini_insercion

    print("Tiempo de ejecución de los algoritmos con " , num_elementos, " elementos\n\n"
    "Tiempo de ejecucion ordenacion por burbuja:", t_burbuja, "\n"
    "Tiempo de ejecucion ordenacion por seleccion:", t_seleccion, "\n"
    "Tiempo de ejecucion ordenacion por mezcla:", t_mezcla, "\n"
    "Tiempo de ejecucion ordenacion por seleccion:", t_insercion, "\n")


def ordenacionBurbuja(lista):
    for i in range(1,len(lista)):
            for j in range(0,len(lista)-i):
                if(lista[j+1] < lista[j]):
                    aux=lista[j]
                    lista[j]=lista[j+1]
                    lista[j+1]=aux
    return lista

def ordenacionSeleccion(lista):
    for i in range(len(lista)):
            minimo=i
            for j in range(i,len(lista)):
                if(lista[j] < lista[minimo]):
                    minimo=j
            if(minimo != i):
                aux=lista[i]
                lista[i]=lista[minimo]
                lista[minimo]=aux
    return lista

def ordenamientoPorMezcla(lista):
    if len(lista)>1:
        mitad = len(lista)//2
        mitadIzquierda = lista[:mitad]
        mitadDerecha = lista[mitad:]

        ordenamientoPorMezcla(mitadIzquierda)
        ordenamientoPorMezcla(mitadDerecha)

        i=0
        j=0
        k=0
        while i < len(mitadIzquierda) and j < len(mitadDerecha):
            if mitadIzquierda[i] < mitadDerecha[j]:
                lista[k]=mitadIzquierda[i]
                i=i+1
            else:
                lista[k]=mitadDerecha[j]
                j=j+1
            k=k+1

        while i < len(mitadIzquierda):
            lista[k]=mitadIzquierda[i]
            i=i+1
            k=k+1

        while j < len(mitadDerecha):
            lista[k]=mitadDerecha[j]
            j=j+1
            k=k+1
    return lista

def ordenacionInsercion(lista):
    for i in range(len(lista)):
            for j in range(i,0,-1):
                if(lista[j-1] > lista[j]):
                    listaux=lista[j]
                    lista[j]=lista[j-1]
                    lista[j-1]=listaux
    return lista

ordenaAleatorio()
