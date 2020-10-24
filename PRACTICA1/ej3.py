#definimos un set por ser una buena estructura de datos para la búsqueda
#haremos pues un bucle que recorra desde el 2 hasta el número dado + 1
#comprobaremos entonces en cada iteraccion que el número que tratamos no
#esté ya en el set, si no lo está añadiremos a nuestro set de múltiplos
#el número considerado y todos sus múltiplos * i desde i^2  * i hasta n

def criba_eratostenes(n):
  multiplos = set()
  for i in range(2, n+1):
    if i not in multiplos:
      print(i, end=" ")
      multiplos.update(range(i*i, n+1, i))