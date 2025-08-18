""" 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!” """

print(f"Hola Mundo!")

""" 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
 el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
 por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
 realizar la impresión por pantalla.  """

nombre = input("¿Cual es tu nombre?")
print(f"Hola", nombre )

""" 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
 imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
 “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizarPep
 la impresión por pantalla. """

nombre2 = input("Cual es tu nombre?")
apellido = input("Cual estu apellido?")
edad = int(input("Cual es tu edad?"))
nacionalidad = input("Cual es tu nacionalidad?")
print(f"Soy", nombre2, apellido, "tengo", edad,  "años y vivo en", nacionalidad )

""" 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro."""

radio = float(input("Ingrese el radio del circulo: "))
pi = 3.1416
area = pi * (radio ** 2)
perimetro = 2 * pi * radio
print(f"Area: {area:.2f}", f"Perimetro: {perimetro:.2f} ")

""" 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
cuántas horas equivale. """
seg = int(input("Ingresa una cantidad de segundos"))
minutos = seg / 60
horas = minutos/60
print(f"La cantidad de horas equivalentes es {horas:.2f}")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
num = int(input("Ingrese un numero para crear su tabla de multiplicaciones"))
print(f"{num}*1:{num*1}")
print(f"{num}*2:{num*2}")
print(f"{num}*3:{num*3}")
print(f"{num}*4:{num*4}")
print(f"{num}*5:{num*5}")
print(f"{num}*6:{num*6}")
print(f"{num}*7:{num*7}")
print(f"{num}*8:{num*8}")
print(f"{num}*9:{num*9}")
print(f"{num}*10:{num*10}")

"""
7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, 
 dividirlos, multiplicarlos y restarlos. """
num1=int(input("Inserte un numero distinto a 0 "))
num2=int(input("Inserte un numero distinto a 0 "))
if num1 == 0 and num2 == 0:
    print("Inserte un numero distinto a 0")
print(f"La suma entre los numeros {num1 +num2}")
print(f"La division entre los numeros {num1 / num2}")
print(f"La multiplicacion entre los numeros {num1 * num2}")
print(f"La resta entre los numeros {num1 - num2}")

""" 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal. """
altura= float(input("Ingrese su altura (Ejemplo 1.78) "))
peso = int(input("Ingrese su peso expresado en kg "))
imc = peso / (altura*2)
if imc<18.5:
    print(f"{imc:.2f} bajo peso")
if imc>=18.5 and imc <24.9:
    print(f"{imc:.2f} Peso normal/saludable")
if imc>=25.0 and imc <29.9:
    print(f"{imc:.2f} Sobrepeso")
if imc>=30.0 and imc <34.9:
    print(f"{imc:.2f} Obesidad grado I")
if imc>=35.0 and imc <39.9:
    print(f"{imc:.2f} Obesidad grado II")
if imc>=40.00:
    print(f"{imc:.2f} Obesidad grado III")

""" 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. """
celcius=int(input("Ingrese una temperatura en Celcius "))
f= (celcius * 9) / 5 + 32
print(f"Su equivalente en Fahrenheit es {f} ")

""" 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números. """

num3 = int(input("Ingrese el primer numero "))
num4 = int(input("Ingrese el segundo numero "))
num5 = int(input("Ingrese el tercero numero "))
promedio = (num3+ num4 + num5) / 3

print(f"El promedio es {promedio}")

