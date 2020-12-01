#./app/app.py
from flask import Flask, url_for, render_template, request, flash, redirect, session
from queue import LifoQueue
import re
import random
from pickleshare import *
from time import time
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'




@app.route('/')
def layout():
    actualizarUltimaPagina("http://localhost:5000","Inicio")
    return render_template("layout.html", titulo="Inicio")


######################################################################################################
######################################################################################################
###############################################EJERCICIO 2############################################
######################################################################################################
######################################################################################################

@app.route('/ejercicio2', methods=["GET"])
def muestraEjercicio2():
    actualizarUltimaPagina("http://localhost:5000///ejercicio2", "Algoritmos de Ordenación")
    return render_template("ejercicio2.html", titulo="Algoritmos de Ordenación")

def actualizarUltimaPagina(url, titulo):
    if 'ultimaspaginas2' in session:
        if session['ultimaspaginas0'] != url and url != "":
            session['ultimaspaginas2']=session['ultimaspaginas1']
            session['ultimaspaginas1']=session['ultimaspaginas0']
            session['ultimaspaginas0']=url
            session['ultimaspaginas2titulo']=session['ultimaspaginas1titulo']
            session['ultimaspaginas1titulo']=session['ultimaspaginas0titulo']
            session['ultimaspaginas0titulo']=titulo
    else:
        session['ultimaspaginas0']="http://localhost:5000///ejercicio2"
        session['ultimaspaginas1']="http://localhost:5000///ejercicio3"
        session['ultimaspaginas2']="http://localhost:5000///ejercicio4"
        session['ultimaspaginas0titulo']="Algoritmos de Ordenación"
        session['ultimaspaginas1titulo']="Criba de Eratóstenes"
        session['ultimaspaginas2titulo']="Fibonacci"
    
    return 0

@app.route('/algoritmos_ordenacion')

def ordenaAleatorio():
    listaOriginal = request.args.get('lista')
    listaOriginal=listaOriginal.split(",")

    for i in range(0, len(listaOriginal)):
        listaOriginal[i]=int(listaOriginal[i])

    tini_burbuja = time() 
    lista = ordenacionBurbuja(listaOriginal)
    tfin_burbuja = time() 
    t_burbuja = tfin_burbuja - tini_burbuja
    
    tini_seleccion = time() 
    lista = ordenacionSeleccion(listaOriginal)
    tfin_seleccion = time() 
    t_seleccion = tfin_seleccion - tini_seleccion

    tini_insercion = time() 
    lista = ordenacionInsercion(listaOriginal)
    tfin_insercion = time() 
    t_insercion = tfin_insercion - tini_insercion

    tini_mezcla = time() 
    lista = ordenamientoPorMezcla(listaOriginal)
    tfin_mezcla = time() 
    t_mezcla = tfin_mezcla - tini_mezcla

    resultado = ["Tiempo de ejecución de los algoritmos con "+ str(len(listaOriginal)) +" elementos", "Tiempo de ejecucion ordenacion por burbuja: " + str(t_burbuja), "Tiempo de ejecucion ordenacion por seleccion: " + str(t_seleccion), "Tiempo de ejecucion ordenacion por mezcla: " + str(t_mezcla), "Tiempo de ejecucion ordenacion por insercion: " + str(t_insercion), "Lista ordenada: " + str(lista)]

    return render_template("ejercicio2.html", titulo="Algoritmos de Ordenación", subtitulo="Resultados Ordenación", lista=resultado)

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

@app.route('/ejercicio3', methods=["GET", "POST"])
def muestraEjercicio3():
    actualizarUltimaPagina("http://localhost:5000///ejercicio3", "Criba de Eratóstenes")
    return render_template("ejercicio3.html", titulo="Criba de Eratóstenes")


@app.route('/criba_eratostenes')

def criba_eratostenes():
    num_elemento = request.args.get('numero')

    if num_elemento!="":
        num_elemento = int(num_elemento)
        resultado=""
        multiplos = set()

        for i in range(2, num_elemento+1):
            if i not in multiplos:
                resultado += str(i) + ", "
                multiplos.update(range(i*i, num_elemento+1, i))
        
        resultado = resultado[:len(resultado)-1]
        resultado = resultado[:len(resultado)-1]

        return render_template("ejercicio3.html", titulo="Criba de Eratóstenes", subtitulo="Resultado de la criba",elemento= "La criba para " + str(num_elemento) + " es: " + "[ " + resultado + "]")        
    else:
        return render_template("ejercicio3.html", titulo="Criba de Eratóstenes", subtitulo="Resultado de la criba",elemento= "No ha introducido ningún elemento!")        



######################################################################################################
######################################################################################################
###############################################EJERCICIO 4############################################
######################################################################################################
######################################################################################################

@app.route('/ejercicio4', methods=["GET", "POST"])
def muestraEjercicio4():
    actualizarUltimaPagina("http://localhost:5000///ejercicio4", "Fibonacci")
    return render_template("ejercicio4.html", titulo="Fibonacci")


@app.route('/fibonacci')
def fib():
    numero = request.args.get('numero')

    if numero!="":
        numero = int(numero)
        a = 0
        b = 1
        
        for k in range(numero):
            c = b+a
            a = b
            b = c

        return render_template("ejercicio4.html", titulo="Fibonacci", subtitulo="Resultado de Fibonacci", elemento= "El término número "+ str(numero) + " es: " + str(a))
    else:
        return render_template("ejercicio4.html", titulo="Fibonacci", subtitulo="Resultado de Fibonacci", elemento= "No ha introducido ningún elemento!")

    

######################################################################################################
######################################################################################################
###############################################EJERCICIO 5############################################
######################################################################################################
######################################################################################################

@app.route('/ejercicio5', methods=["GET", "POST"])
def muestraEjercicio5():
    actualizarUltimaPagina("http://localhost:5000///ejercicio5", "Comprobador de Cadenas")
    return render_template("ejercicio5.html", titulo="Comprobador de Cadenas")


@app.route('/comprueba_cadena')

def checkCadena():
    lista = request.args.get('lista')
    lista=lista.split(",")

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
        return render_template("ejercicio5.html", titulo="Resultado del Comprobador de Cadenas", subtitulo="Resutado", resultado="La cadena " + str(lista) + " es correcta")
    else:
        return render_template("ejercicio5.html", titulo="Resultado del Comprobador de Cadenas", subtitulo="Resutado", resultado="La cadena " + str(lista) + " no es correcta")
######################################################################################################
######################################################################################################
###############################################EJERCICIO 6############################################
######################################################################################################
######################################################################################################

@app.route('/ejercicio6', methods=["GET", "POST"])
def muestraEjercicio6():
    actualizarUltimaPagina("http://localhost:5000///ejercicio6", "Comprobador de Expresiones")
    return render_template("ejercicio6.html", titulo="Comprobador de Expresiones")


@app.route('/exp_regular')
def compruebaExpresion():
    tipo=""
    expresion = request.args.get('expresion')


    if(re.match(r"[\w\s]+[A-Z]", expresion)): 
        tipo = "La expresión es una palabra seguida de un espacio y una única letra mayúscula"
    elif(re.match(r"^[_a-z0-9-]+(.[_a-z0-9-]+)@[a-z0-9-]+(.[a-z0-9-]+)(.[a-z]{2,3})$", expresion)):
        tipo = "La expresión es un correo electrónico"
    elif(re.match(r"^\d{4}([\ -]?)\d{4}\1\d{4}\1\d{4}$", expresion)):
        tipo = "La expresión es una tarjeta de crédito"
    else:
        tipo="Expresión desconocida"

    return render_template("ejercicio6.html", titulo="Comprobador de Expresiones", subtitulo="Resultado de la comprobación de cadenas", resultado=tipo)

######################################################################################################
######################################################################################################
###############################################APP SVG############################################
######################################################################################################
######################################################################################################

@app.route('/ejercicioSVG')
def muestraEjercicioSVG():
    actualizarUltimaPagina("http://localhost:5000///ejercicioSVG", "Mostrar Figuras SVG Aleatorias")
    elemento=generaFiguraAleatoria() + generaFiguraAleatoria()
    return render_template("svg.html", titulo="Mostrar Figuras SVG Aleatorias", content=elemento)


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

######################################################################################################
######################################################################################################
##################################################LOGIN###############################################
######################################################################################################
######################################################################################################

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user =request.form.get('User')
        password = request.form.get('Password')

        if checkUser(user, password):
            session['user'] = user
            session['password'] = password
            message = 'Logeado en el sistema, bienvenido ' + session['user']
            flash(message)

            return redirect(url_for('layout'))
        else:
            error = 'Las credenciales no corresponden a ningún usuario del sistema'
            flash(error)
            return redirect(url_for('layout'))

def checkUser(user, password):
    db = PickleShareDB('data/')
    registrado=False

    if user in db:
        if db[user]['password']==password:
            registrado=True

    return registrado

@app.route('/log-out', methods=['GET', 'POST'])
def logout():
    session.pop('user',None)
    session.pop('password',None)
    mensaje="Ha salido del sistema"
    flash(mensaje)
    
    return redirect(url_for('layout')) 
######################################################################################################
######################################################################################################
##############################################DATOS USUARIO###########################################
######################################################################################################
######################################################################################################

@app.route('/datos-sesion/<string:mostrar>',methods=['GET'])
def datos_sesion(mostrar):
    if 'user' in session:
        user = session['user']
    else:
        user = ''

    if 'password' in session:
        password = session['password']
    else:
        password = ''

    if mostrar == 'editar':
        return render_template('gestionaDatosUsuario.html', titulo="Datos del Usuario", user=user, password=password)
    elif mostrar == 'registrarse':
        return render_template('gestionaDatosUsuario.html', titulo="Registro de un nuevo usuario")
    else:
        return render_template('gestionaDatosUsuario.html', titulo="Datos del Usuario",  disabled="disabled", user=user, password=password)

@app.route('/insertarUsuario',methods=['POST'])
def nuevoUsuario():
    user =request.form.get('User')
    password = request.form.get('Password')
    db = PickleShareDB('data/')

    if user in db:
        respuesta = "Este usuario está en uso!"
        flash(respuesta)

        return redirect(url_for('layout'))
    elif user=="" or password=="":
        respuesta = "No puede dejar el vacíos el campo usuario o contraseña, inténtelo de nuevo"
        flash(respuesta)

        return redirect(url_for('layout'))
    else:
        db[user]=dict()
        db[user]['password']=password
        db[user]=db[user]
        respuesta = "Usuario registrado con éxito!"
        flash(respuesta)

        return redirect(url_for('layout'))
    
@app.route('/editarDatos',methods=['POST'])
def editarUsuario():
    user =request.form.get('User')
    password = request.form.get('Password')
    db = PickleShareDB('data/')

    if (user!=session['user']) and user in db:
            respuesta = "Este usuario está en uso!"
            flash(respuesta)

            return redirect(url_for('layout'))
    elif user=="" or password=="":
        respuesta = "No puede dejar el vacíos el campo usuario o contraseña, inténtelo de nuevo"
        flash(respuesta)

        return redirect(url_for('layout'))
    else:
        del db[session['user']]
        db[user]=dict()
        db[user]['password']=password
        db[user]=db[user]
        session['user']=user
        session['password']=password
        respuesta = "Usuario editado con éxito!"
        flash(respuesta)        

        return redirect(url_for('layout'))

######################################################################################################
######################################################################################################
################################################ERROR PAGE############################################
######################################################################################################
######################################################################################################

@app.errorhandler(404)
def page_not_found(error):
    return "<h1>404 Page Not Found</h1><h2>No se ha podido encotrar la página que buscaba :/ </h2>", 404

with app.test_request_context():
    print(url_for('static', filename='mainpage.html'))