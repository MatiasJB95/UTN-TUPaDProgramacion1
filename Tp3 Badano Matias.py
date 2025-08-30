'''1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. '''

edad= int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

''' 
2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”. '''

notaString = int(input("Ingresa su nota: "))
if notaString >= 6:
    print("Aprobado")
else:
    6
    print("desaprobado") 


'''3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
operador de módulo (%) en Python para evaluar si un número es par o impar. '''

numeroPar = int(input("Ingrese un numero Par: "))
numMod = numeroPar % 2
if numMod == 0 :
   print("Ha ingresado un número par")
else: 
   print("Por favor, ingrese un número par")

'''4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años.'''

edad1 = int(input("Ingrese la edad: "))

if edad1 < 12 :
    print("Pertenece a la categoria de Niño/a")
elif edad1 >= 12 and edad1 <=18 :
    print("Pertenece a la categoria de Adolescente") 
elif edad1 >= 18 and edad1 < 30:
    print("Pertenece a la categoria de Adulto") 
else:
    print("Adulto/a: mayor")

'''5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string'''

contrasena = input("Ingrese una contraseña: ")

if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


'''6) Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
Definir la lista numeros_aleatorios de la siguiente forma: '''  

import random
from statistics import mean, median, mode
numerosAleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numerosAleatorios)
mediana = median(numerosAleatorios)
moda = mode(numerosAleatorios)

print("Lista de números:", numerosAleatorios)
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

if media > mediana > moda:
    print("La distribución tiene sesgo positivo.")
elif media < mediana < moda:
    print("La distribución tiene sesgo negativo.")
elif media == mediana == moda:
    print("La distribución no tiene sesgo.")
else:
    print("La distribución no cumple con los criterios de sesgo.")  

''' 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla.''' 
     
texto = input("Ingrese una palabra o frase: ")

if texto[-1].lower() in "aeiou":
    texto += "!"
    
print("Resultado:", texto) 

'''Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
lower() y title() de Python para convertir entre mayúsculas y minúsculas. ''' 

nombre = input("Ingrese su nombre: ")
print("Elija una opcion:")
print("1. Mostrar en mayuscula")
print("2. Mostrar en minusculas")
print("3. Mostrar con la primera letra en mayúscula")

opcion = input("Ingrese 1, 2 o 3: ")

if opcion == "1":
    print("Resultado:", nombre.upper())
elif opcion == "2":
    print("Resultado:", nombre.lower())
elif opcion == "3":
    print("Resultado:", nombre.title())
else:
    print("Opción inválida. Por favor ingrese 1, 2 o 3.")

'''9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).'''

magnitud = float(input("Ingrese la magnitud del terremoto en la escala de Richter: "))
if magnitud < 3:
    print("Muy leve. Imperceptible.")
elif 3 <= magnitud < 4:
    print("Leve. Ligeramente perceptible")
elif 4 <= magnitud < 5:
    print("Moderado.  Sentido por personas, pero generalmente no causa daños")
elif 5 <= magnitud < 6:
    print("Fuerte. Puede causar daños en estructuras debiles")
elif 6 <= magnitud < 7:
    print("Muy Fuerte. Puede causar daños significativos")
else:  
    print("Extremo. Puede causar graves daños a gran escala")

''' 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano.'''
hemisferio = input("Ingrese el hemisferio (N para Norte S para Sur): ").upper()
mes = input("Ingrese el mes: ").lower()
dia = int(input("Ingrese el día: "))

meses = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4,
    "mayo": 5, "junio": 6, "julio": 7, "agosto": 8,
    "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
}

numMes = meses.get(mes)

if numMes is None:
    print("Mes invalido")
else:
    fecha = (numMes, dia)

    estacion = ""

    if hemisferio == "N":
        if (fecha >= (3, 21)) and (fecha < (6, 21)):
            estacion = "Primavera"
        elif (fecha >= (6, 21)) and (fecha < (9, 23)):
            estacion = "Verano"
        elif (fecha >= (9, 23)) and (fecha < (12, 21)):
            estacion = "Otoño"
        else:
            estacion = "Invierno"
    elif hemisferio == "S":
        if (fecha >= (3, 21)) and (fecha < (6, 21)):
            estacion = "Otoño"
        elif (fecha >= (6, 21)) and (fecha < (9, 23)):
            estacion = "Invierno"
        elif (fecha >= (9, 23)) and (fecha < (12, 21)):
            estacion = "Primavera"
        else:
            estacion = "Verano"
    else:
        print("Hemisferio inválido (debe ser N o S)")

    if estacion:
        print(f"En el hemisferio {hemisferio} el {dia} de {mes} es {estacion}")