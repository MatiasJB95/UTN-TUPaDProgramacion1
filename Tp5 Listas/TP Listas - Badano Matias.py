"""1) Crear una lista con las notas de 10 estudiantes.
• Mostrar la lista completa.
• Calcular y mostrar el promedio.
• Indicar la nota más alta y la más baja. """
notas = []
for i in range(10):
    nota = float(input(f"Ingrese la nota del estudiante {i+1}: "))
    notas.append(nota)

    print("\nLista de notas")
for i in range(len(notas)):
    print(f"Estudiante {i+1}: {notas[i]}")
suma = 0
for nota in notas:
    suma += nota
promedio = suma / len(notas)
print(f"\nPromedio de notas: {promedio:.2f}")
mayor = notas[0]
menor = notas[0]
for nota in notas:
    if nota > mayor:
        mayor = nota
    if nota < menor:
        menor = nota

print(f"Nota mas alta: {mayor}")
print(f"Nota mas baja: {menor}")

"""
2) Pedir al usuario que cargue 5 productos en una lista.
• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
• Preguntar al usuario qué producto desea eliminar y actualizar la lista.

"""

productos = []
for i in range(5):
    prod = input(f"Ingrese el producto {i+1}: ")
    productos.append(prod)

ordenada = sorted(productos)

print("\nLista de productos ordenada")
for i in range(len(ordenada)):
    print(f"{i+1}. {ordenada[i]}")
eliminar = input("\nIngrese el nombre del producto que desea eliminar: ")

if eliminar in productos:
    productos.remove(eliminar)
    print(f"\n'{eliminar}' fue eliminado de la lista.")
else:
    print(f"\nEl producto '{eliminar}' no se encuentra en la lista.")

print("\nLista actualizada")
for i in range(len(productos)):
    print(f"{i+1}. {productos[i]}")


"""3)Generar una lista con 15 números enteros al azar entre 1 y 100.
• Crear una lista con los pares y otra con los impares.
• Mostrar cuántos números tiene cada lista."""

import random

numeros = []
for i in range(15):
    n = random.randint(1, 100)
    numeros.append(n)

pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("\nLista completa")
for i in range(len(numeros)):
    print(f"{i+1}: {numeros[i]}")

print("\nLista de pares")
for p in pares:
    print(p)

print("\nLista de impares")
for im in impares:
    print(im)
print(f"\nCantidad de pares: {len(pares)}")
print(f"Cantidad de impares: {len(impares)}") 

"""
4) Dada una lista con valores repetidos:
• Crear una nueva lista sin elementos repetidos.
• Mostrar el resultado.
"""

datos = [5, 3, 8, 3, 5, 2, 8, 9, 1, 2, 5, 7]

sinRepetidos = []

for elemento in datos:
    if elemento not in sinRepetidos:
        sinRepetidos.append(elemento)

print("\nLista sin repetidos")
for elemento in sinRepetidos:
    print(elemento)

"""5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
• Mostrar la lista final actualizada."""

estudiantes = ["Pedro","Juan","Mateo","Maria","Florencia","Lourdes","Valquiria","Lucas"]

accion = input("Escriba 'agregar' o 'eliminar': ").strip().lower()

if accion == "agregar":
    nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
    print(f"\nSe agregó '{nuevo}' a la lista.")

elif accion == "eliminar":
    eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
        print(f"\nSe eliminó '{eliminar}' de la lista.")
    else:
        print(f"\nEl estudiante '{eliminar}' no está en la lista.")

else:
    print("\nAccion Invalida")

print("\nLista final de estudiantes")
for estudiante in estudiantes:
    print(estudiante)

"""
6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
último pasa a ser el primero).
"""

numeros = [10, 20, 30, 40, 50, 60, 70]

print("Lista original:")
for n in numeros:
    print(n, end=" ")

ultimo = numeros[-1]
rotada = [ultimo] + numeros[:-1]

print("\n\nLista rotada a la derecha:")
for n in rotada:
    print(n, end=" ")

"""
7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
semana.
• Calcular el promedio de las mínimas y el de las máximas.
• Mostrar en qué día se registró la mayor amplitud térmica."""

temperaturas = [
    [8, 12],
    [7, 14],
    [10, 14],
    [11, 16],
    [14, 20],
    [14, 21],
    [6, 10]
]

sumaMin = 0
sumaMax = 0

for dia in temperaturas:
    sumaMin += dia[0]
    sumaMax += dia[1]

prom_min = sumaMin / len(temperaturas)
prom_max = sumaMax / len(temperaturas)

mayorAplitud = 0
diaMayorTemp = 0

for i in range(len(temperaturas)):
    amplitud = temperaturas[i][1] - temperaturas[i][0]
    if amplitud > mayorAplitud:
        mayorAplitud = amplitud
        diaMayorTemp = i + 1 

# Mostrar resultados
print(f"Promedio de minimas: {prom_min:.2f}")
print(f"Promedio de maximas: {prom_max:.2f}")
print(f"El dia {diaMayorTemp} tuvo la mayor amplitud térmica ({mayorAplitud}°C).")

"""
8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
• Mostrar el promedio de cada estudiante.
• Mostrar el promedio de cada materia.
"""

notas = [
    [10, 9, 8],
    [5, 9, 7],
    [4, 7, 9],
    [8, 7, 5],
    [9, 8, 10]
]

print("Promedio de cada estudiante:")
for i in range(len(notas)):
   sumaEst = sum(notas[i])
   promEst =sumaEst / len(notas[i])
   print(f"Estudiante {i+1}: {promEst:.2f}")

print("\nPromedio de cada materia:")
materias = len(notas[0])

for j in range(materias):
    sumaMat = 0
    for i in range(len(notas)):
        sumaMat += notas[i][j]
    promMat = sumaMat / len(notas)
    print(f"Materia {j+1}: {promMat:.2f}")

"""9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
• Inicializarlo con guiones "-" representando casillas vacías.
• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
• Mostrar el tablero después de cada jugada."""
tablero = [["-"] * 3 for _ in range(3)]

def mostrarTablero(tab):
    for fila in tab:
        print(" ".join(fila))
    print()

print("Tablero inicial:")
mostrarTablero(tablero)

for turno in range(9):
    if turno % 2 == 0:
        jugador = "X"
    else:
        jugador = "O"

    print(f"Turno del jugador {jugador}")
    fila = int(input("Ingrese fila (0-2): "))
    columna = int(input("Ingrese columna (0-2): "))

    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
    else:
        print("Casilla ocupada, pierdes el turno.")

    mostrarTablero(tablero)

"""
10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
• Mostrar el total vendido por cada producto.
• Mostrar el día con mayores ventas totales.
• Indicar cuál fue el producto más vendido en la semana.
"""
ventas = [
    [5, 3, 4, 6, 2, 7, 8],
    [2, 4, 6, 3, 5, 7, 9],
    [8, 6, 4, 5, 3, 2, 1],
    [7, 5, 3, 6, 4, 8, 10]
]

print("Total vendido por cada producto:")
for i in range(len(ventas)):
    totalProd = sum(ventas[i])
    print(f"Producto {i+1}: {totalProd}")

diasTotales = []
for j in range(7):
   sumaDias = 0
   for i in range(4):
       sumaDias += ventas[i][j]
       diasTotales.append(sumaDias)

maxDia = max(diasTotales)
diaMayor = diasTotales.index(maxDia) + 1

print(f"\nEl dia con mayores ventas fue el dia {diaMayor} con {maxDia} ventas.")

totalesProd = [sum(fila) for fila in ventas]
prodMax = max(totalesProd)
productoMasVendido = totalesProd.index(prodMax) + 1

print(f"El producto mas vendido en la semana fue el Producto {productoMasVendido} con {prodMax} ventas.")