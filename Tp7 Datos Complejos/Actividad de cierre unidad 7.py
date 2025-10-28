"""
1) Dado el diccionario precios_frutas precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
Añadir las siguientes frutas con sus respectivos precios: ● Naranja = 1200 ● Manzana = 1500 ● Pera = 2300
"""
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)
"""
2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes 
frutas: ● Banana = 1330 ● Manzana = 1700 ● Melón = 2800
"""
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera':2300}
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

""" 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios."""

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera':2300}
solo_frutas = list(precios_frutas.keys())
print(solo_frutas)
"""
4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe."""

contactos = {}
for _ in range(5):
    nombre = input("Nombre: ").strip()
    numero = input("Numero: ").strip()
    contactos[nombre] = numero

consulta = input("Ingresa un nombre para consultar: ").strip()
if consulta in contactos:
    print(f"Numero de {consulta}: {contactos[consulta]}")
else:
    print("No se encontro el contacto.")

"""5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra.
"""
frase = input("Ingresa una frase: ").lower()
palabras = frase.split()

unicas = set(palabras)
print("Palabras unicas:", unicas)

frecuencias = {}
for p in palabras:
    frecuencias[p] = frecuencias.get(p, 0) + 1
print("Frecuencia:", frecuencias)

"""6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno"""
alumnos = {}

for i in range(3):
    nombre = input(f"Nombre del alumno {i+1}: ").strip()
    notas_str = input("Ingresa 3 notas separadas por espacio: ")
    nota1, nota2, nota3 = map(float, notas_str.split())
    alumnos[nombre] = (nota1, nota2, nota3)

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: promedio = {promedio:.2f}")

"""7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 
"""

parcial1 = {"Ana", "Luis", "Marta", "Sofía", "Juan"}
parcial2 = {"Marta", "Sofía", "Pedro", "Lucía", "Ana"}

ambos = parcial1 & parcial2
solo_uno = (parcial1 ^ parcial2)
al_menos_uno = (parcial1 | parcial2)

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

"""8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe.
"""

stock = {
    "lapiz": 10,
    "cuaderno": 5,
    "goma": 3
}

prod = input("Producto a consultar/agregar: ").strip().lower()
if prod in stock:
    print(f"Stock actual de {prod}: {stock[prod]}")
    try:
        inc = int(input("Unidades a agregar: "))
        stock[prod] += inc
        print(f"Nuevo stock de {prod}: {stock[prod]}")
    except ValueError:
        print("Ingresa un numero entero.")
else:
    try:
        unidades = int(input(f"{prod} no existe. Unidades iniciales: "))
        stock[prod] = unidades
        print(f"Agregado {prod} con {unidades} unidades.")
    except ValueError:
        print("Ingresa un numero entero.")

print("Stock actual:", stock)


"""
9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos
"""

agenda = {}
for _ in range(3):
    dia = input("Día: ").strip().title()
    hora = input("Hora: ").strip()
    evento = input("Evento: ").strip()
    agenda[(dia, hora)] = evento


cdia = input("Consultar - Día: ").strip().title()
chora = input("Consultar - Hora: ").strip()
evento = agenda.get((cdia, chora))
if evento:
    print(f"En {cdia} a las {chora}: {evento}")
else:
    print("No hay evento en ese día y hora.")

"""10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores
"""
paises_a_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"
}

capitales_a_paises = {capital: pais for pais, capital in paises_a_capitales.items()}
print(capitales_a_paises)