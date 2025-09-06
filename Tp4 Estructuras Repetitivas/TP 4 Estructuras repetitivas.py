"""1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea"""

for i in range (1, 101):
    print(i)

""" 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene. """ 

num = int(input("Ingrese un numero entero: "))
cantidadDigitos = len(str(abs(num)))

print(f"Tiene {cantidadDigitos} digito/s.")

""" 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores. 
"""
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

menor = min(num1, num2)
mayor = max(num1, num2)

suma = sum(range(menor + 1, mayor))

print(f"La suma de los numeros enteros entre {num1} y {num2} es: {suma}")

"""4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0."""

suma = 0
while True:
    numero = int(input("Ingrese un numero entero,  0 para terminar "))
    if numero == 0:
        break
    suma += numero
print(f"La suma total es: {suma}") 

"""5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""

import random
secreto = random.randint(0, 9)

intentos = 0
adivinanza = -1
print("Juego: Adivina el numero (entre 0 y 9)")

while adivinanza != secreto:
    adivinanza = int(input("Ingrese su numero: "))
    intentos += 17

print(f"Felicidades! El numero era {secreto}.")
print(f"Adivinaste en {intentos} intento/s.")

"""6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente. """

for i in range(100, -1, -2):
    print(i)

"""7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.  """

num3 = int(input("Ingrese un numero entero positivo: "))

suma = 0

for i in range(num3 + 1):
    suma += i

print(f"La suma de los números de 1 a {num3} es: {suma}")

"""
8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio)
"""

cantidad = 100

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(cantidad):
    numero = int(input(f"Ingrese el numero {i+1}: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("Resultados")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")

"""9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor)."""

cantidad1 = 100
suma = 0

for i in range(cantidad1):
    numero = int(input(f"Ingrese el numero {i+1}: "))
    suma += numero

media = suma / cantidad1

print(f"\nLa media de los {cantidad1} numeros ingresados es: {media}")

"""10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745"""

num4 = input("Ingrese un numero entero: ")

invertido = num4[::-1] 

print(f"El numero invertido es: {invertido}")