#./app/app.py
from flask import Flask, url_for
from queue import LifoQueue
import re
import random
from time import time
app = Flask(__name__)
          
#url_for('static', filename='mainpage.html')

@app.route('/')
def hello_world():
	return 'Hello, World!'

######################################################################################################
######################################################################################################
###############################################EJERCICIO 2############################################
######################################################################################################
######################################################################################################

@app.route('/algoritmos_ordenacion/<string:numeros>')

def ordenaAleatorio(numeros):
    lista=numeros.split(",")

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

    resultado = "Tiempo de ejecución de los algoritmos con "+ str(len(lista)) +" elementos\n\n" + "Tiempo de ejecucion ordenacion por burbuja: " + str(t_burbuja) + "\n" + "Tiempo de ejecucion ordenacion por seleccion: " + str(t_seleccion) + "\n" + "Tiempo de ejecucion ordenacion por mezcla: " + str(t_mezcla) + "\n" + "Tiempo de ejecucion ordenacion por insercion: " + str(t_insercion)

    return resultado

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

######################################################################################################
######################################################################################################
###############################################EJERCICIO 3############################################
######################################################################################################
######################################################################################################

@app.route('/criba_eratostenes/<int:num_elemento>')

def criba_eratostenes(num_elemento):
    resultado=""
    multiplos = set()

    for i in range(2, num_elemento+1):
        if i not in multiplos:
            resultado += str(i) + " "
            multiplos.update(range(i*i, num_elemento+1, i))
    
    return resultado        

######################################################################################################
######################################################################################################
###############################################EJERCICIO 4############################################
######################################################################################################
######################################################################################################

@app.route('/fibonacci/<int:numero>')

def fib(numero):
    a = 0
    b = 1
    
    for k in range(numero):
        c = b+a
        a = b
        b = c
        
    return str(a)

######################################################################################################
######################################################################################################
###############################################EJERCICIO 5############################################
######################################################################################################
######################################################################################################

@app.route('/comprueba_cadena/<string:cadena>')


def checkCadena(cadena):
    lista=cadena.split(",")

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
        return str(lista) + "\n" + str(True)
    else:
        return str(lista) + "\n" + str(False)
######################################################################################################
######################################################################################################
###############################################EJERCICIO 6############################################
######################################################################################################
######################################################################################################

@app.route('/exp_regular/<string:expresion>')

def compruebaExpresion(expresion):
    tipo=""

    if(re.match(r"[\w\s]+[A-Z]", expresion)): 
        tipo = "La expresión es una palabra seguida de un espacio y una única letra mayúscula"
    elif(re.match(r"^[_a-z0-9-]+(.[_a-z0-9-]+)@[a-z0-9-]+(.[a-z0-9-]+)(.[a-z]{2,3})$", expresion)):
        tipo = "La expresión es un correo electrónico"
    elif(re.match(r"^\d{4}([\ -]?)\d{4}\1\d{4}\1\d{4}$", expresion)):
        tipo = "La expresión es una tarjeta de crédito"
    else:
        tipo="Expresión desconocida"

    return tipo

######################################################################################################
######################################################################################################
###############################################APP SVG############################################
######################################################################################################
######################################################################################################

@app.route('/svg')
def dibujaSVG():
    pagina="<!DOCTYPE html> <html> <head><title>APP SVG</title><meta charset='UTF-8'><meta name='title' content='APP SVG'><link href='static/hoja-estilo.css' rel='stylesheet' type='text/css'/></head><body id='contenedor'><header id='cabecera'><!-- Main content --><h1 id='title'>APP SVG</h1></header><div id='figura'>"
    pagina2= "</div><footer id='piepagina'><small>David Heredia Cortés</small><small>Desarrollo de Aplicaciones para Internet</small><small>Octubre, 2020</small></footer></body></html>"
    elemento=generaFiguraAleatoria() + generaFiguraAleatoria()

    return pagina + elemento + pagina2


def getRandomColor():
    r = lambda: random.randint(0,255)
    return('#%02X%02X%02X' % (r(),r(),r()))


def generaFiguraAleatoria():
    tipo= random.randint(0,5)

    if(tipo==0):
        figura=generaCuadrado()
    elif(tipo==1):
        figura=generaCuadradoCirc()
    elif(tipo==2):
        figura=generaCirculo()
    elif(tipo==3):
        figura=generaEstrella()
    elif(tipo==4):
        figura=generaElipse()
    else:
        figura=generaPicos()

    return figura

def generaCuadrado():
    width=random.randint(10,400)
    height=random.randint(10,400)

    color=getRandomColor()
    cuadrado="<svg><rect x='10' y='10' width='"+ str(width) +"' height='"+ str(height) +"' fill='"+ color +"' /></svg>"

    return cuadrado

def generaCuadradoCirc():

    width=random.randint(10,400)
    height=random.randint(10,400)
    rx=random.randint(0,50)
    ry=random.randint(0,50)
    color=getRandomColor()

    cuadradocirc="<svg width='"+ str(width+20) +"' height='"+ str(height+20) +"'><rect x='10' y='10' width='"+ str(width) +"' height='"+ str(height) +"' rx='"+ str(rx) +"' ry='"+ str(ry) +"' fill='"+ color +"' /></svg>"

    return cuadradocirc

def generaElipse():
    rx=random.randint(20,300)
    ry=random.randint(20,300)
    color=getRandomColor()

    elipse="<svg width='"+ str(2*rx) +"' height='"+ str(2*ry) +"'> <ellipse cx='"+ str(rx) +"' cy='"+ str(ry) +"' rx='"+ str(rx) +"' ry='"+ str(ry) +"' fill='"+ color +"' /></svg>"

    return elipse

def generaEstrella():
    color=getRandomColor()
    stroke=getRandomColor()
    stroke_width=random.randint(0,20)

    estrella="<svg width='250' height='215'> <polygon fill='"+ str(color) +"' stroke='"+ str(stroke) +"' stroke-width='"+ str(stroke_width) +"' points='129,150 85,119 41,150 57,104 15,66 68,66 85,15 102,65 156,66 113,98' /> </svg>"
    
    return estrella

def generaPicos():
    color1=getRandomColor()
    stroke1=getRandomColor()
    stroke_width1=random.randint(0,20)

    color2=getRandomColor()
    stroke2=getRandomColor()
    stroke_width2=random.randint(0,20)

    color3=getRandomColor()
    stroke3=getRandomColor()
    stroke_width3=random.randint(0,20)

    picos="<svg width='130' height='130'><polyline points='10,50 65,20 120,50' fill='"+ str(color1) +"' stroke-width='"+ str(stroke_width1) +"' stroke='"+ str(stroke1) +"' stroke-linejoin='miter' /><polyline points='10,85 65,55 120,85' fill='"+ str(color2) +"'stroke-width='"+ str(stroke_width2) +"' stroke='"+ str(stroke2) +"' stroke-linejoin='round' /><polyline points='10,120 65,90 120,120' fill='"+ str(color3) +"'stroke-width='"+ str(stroke_width3) +"' stroke='"+ str(stroke3) +"' stroke-linejoin='bevel' /></svg>"
    
    return picos

def generaCirculo():
    color=getRandomColor()
    stroke=getRandomColor()
    stroke_width=random.randint(0,20)
    radio=random.randint(5,200)

    circulo="<svg  width='"+ str(radio*3) +"' height='"+ str(radio*3) +"'><circle cx='"+ str(radio*1.5) +"' cy='"+ str(radio*1.5) +"' r='"+ str(radio) +"' fill='"+ str(color) +"' stroke='"+ str(stroke) +"' stroke-width='"+ str(stroke_width) +"'></svg>"

    return circulo

@app.errorhandler(404)

def page_not_found(error):
    return "<h1>404 Page Not Found</h1><h2>No se ha podido encotrar la página que buscaba :/ </h2>", 404

with app.test_request_context():
    print(url_for('static', filename='mainpage.html'))