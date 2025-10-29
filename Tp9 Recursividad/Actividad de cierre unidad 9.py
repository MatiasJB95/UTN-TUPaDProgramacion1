""" 
1)  Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario
""" 

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("El factorial no esta definido para negativos.")
    return 1 if n == 0 else n * factorial(n - 1)

N = int(input("Ingresá un numero entero positivo: "))
for i in range(1, N + 1):
    print(f"factorial({i}) = {factorial(i)}")
""" 
2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique.
""" 

def fib(num: int) -> int:
    if num < 0:
        raise ValueError("El numero debe ser >= 0")
    if num in (0, 1):
        return num
    return fib(num - 1) + fib(num - 2)

N = int(input("Ingresa la posición del numero para la serie de Fibonacci: "))
serie = [fib(i) for i in range(N + 1)]
print("Serie de Fibonacci hasta Numero:", serie)

""" 
3) Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula 𝑛
𝑚 = 𝑛 ∗ 𝑛
(𝑚−1)
. Prueba esta función en un
algoritmo general.
    """

def potencia(base: float, exp: int) -> float:
    if exp < 0:
        return 1 / potencia(base, -exp)
    if exp == 0:
        return 1
    return base * potencia(base, exp - 1)

print(potencia(2, 5))
print(potencia(3, 0))
print(potencia(5, 3))

"""
4)Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.
"""

def a_binario(n: int) -> str:
    if n < 0:
        raise ValueError("Usar numeros enteros >= 0")
    if n == 0:
        return "0"
    def rec(x: int) -> str:
        if x == 0:
            return ""
        return rec(x // 2) + str(x % 2)
    return rec(n)

print(a_binario(20))  
"""


5)Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.
"""

def es_palindromo(palabra: str) -> bool:
    def rec(s: str, i: int, j: int) -> bool:
        if i >= j:
            return True
        if s[i] != s[j]:
            return False
        return rec(s, i + 1, j - 1)
    return rec(palabra, 0, len(palabra) - 1)

print(es_palindromo("reconocer"))
print(es_palindromo("parcial"))

"""
6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.
"""
def suma_digitos(nu: int) -> int:
    if nu < 0:
        raise ValueError("Usar numeros enteros positivos 0.")
    if nu < 10:
        return nu
    return (nu % 10) + suma_digitos(nu // 10)
print(suma_digitos(1234)) 
print(suma_digitos(9))     
print(suma_digitos(305)) 

"""
7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.
"""

def contar_bloques(numb: int) -> int:
    if numb < 0:
        raise ValueError("n debe ser >= 0")
    if numb == 0:
        return 0
    return numb + contar_bloques(numb - 1)

print(contar_bloques(1)) 
print(contar_bloques(2))  
print(contar_bloques(4))  


"""
8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.
"""
def contar_digito(numeros: int, digito: int) -> int:
    if numeros < 0 or not (0 <= digito <= 9):
        raise ValueError("numero debe ser >= 0 y digito entre 0 y 9.")
    if numeros < 10:
        return 1 if numeros == digito else 0
    return (1 if numeros % 10 == digito else 0) + contar_digito(numeros // 10, digito)

print(contar_digito(12233421, 2))  
print(contar_digito(5555, 5))   
print(contar_digito(123456, 7))   