# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
# de cada letra en la cadena. Los espacios no deben ser considerados.

def frecuencia_letras(texto):
    frecuencias = {}
    for letra in texto:
        if letra != " ":
            frecuencias[letra] = frecuencias.get(letra, 0) + 1
    return frecuencias

print(frecuencia_letras("You can do it"))


#2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

numeros = [4, 6, 8, 10]
numero_doble = list(map(lambda x : x * 2, numeros))
print(numero_doble)

# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. 
# La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo

lista_ingredients = ["salt", "black pepper", "white pepper", "pepperoni", "mozzarella", "tomato", "flour"]

def ingredients_list(lista_ingredients, ingredient):
    resultado = []

    for ingredients in lista_ingredients:
        if ingredient in ingredients:
            resultado.append(ingredients)

    return resultado

print(ingredients_list(lista_ingredients, "pepper"))

# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

list1 = [20, 40, 60, 80, 100]
list2 = [10, 20, 30, 40, 50]

def difference(list1,list2):
    return (list(map(lambda x, y: x - y, list1, list2)))

print(difference(list1,list2))
print(difference(list1,list1))
print(difference(list2,list1))

# additional one: try to check if the fomula indeed work when you want to verify new conditions
list3 = [3000, 4000, 50000]
list4 = [50, 70, 999]
print(difference(list3, list4))

# 5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
# defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
# que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
# una tupla que contenga la media y el estado.

notas = [10, 5, 4, 6, 7, 10, 4, 3, 2, 5, 6, 7, 2, 9, 8, 6, 7, 4, 3]

def verify_grades(notas, aprovado=5):
    media = round(sum(notas) / len(notas), 2)

    if media >= aprovado:
        status = "aprovado".upper()
    else:
        status = "suspenso".upper()
    return (media, status)

print(verify_grades(notas))

# note: I din´t like the result with many decimals, so I looked a way to improve it. Applied round in the media calculation
# Also, I wanted the status in upper case, applied upper in the string for the status.
# check if the formula can be used in another list 

notas2 = [50, 40, 60, 42, 40, 31, 30, 22, 19, 32]
print(verify_grades(notas2))

notas3 = [2, 2, 1, 4, 1, 3, 5,]
print(verify_grades(notas3))

# 6. Escribe una función que calcule el factorial de un número de manera recursiva.
# Note: I didn´t undestood this one, needed to check online for support

def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))


# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

lista_tuple = [("Peter", "Age", "-", 15), ("Daniel", "Age", "-", 20), ("Sofia", "Age", "-", 30)]

def convert_tuple(lista_tuple):
    return list(map(lambda t: " ".join(map(str, t)), lista_tuple))

print(convert_tuple(lista_tuple))

# note: I have issues, cause I have include the numbers in the tuple, so I needed to work on the join(map)
# created a new funcion for tuples having only strings, no numbers
tuple_str = [("Peter", "Carter"), ("Bruce", "Wayne"), ("Elizabeth", "Taylor")]
def convert_tuplestr(tuple_str):
    return list(map(lambda t: " ".join(t),tuple_str))

print(convert_tuplestr(tuple_str))

# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
# o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
# indicando si la división fue exitosa o no.

try:
    num1 = int(input("Indicate the first number with no decimals: "))
    num2 = int(input("Indicate the sencond number with no decilamls: "))

    resultado = num1 / num2

    print("Successful result")
    print(f"Result: {resultado}")

except ValueError:
    print("Error: Please introduce only numeric values, with no decimal")

except ZeroDivisionError:
    print("Error: Cannot divide by 0")


# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
# excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
# "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

list_animals = ["Tortuga", "Mapache", "Tigre", "Oso", "Gato", "Perro", "Oveja", "Cabra", "Cavallo"]

def filtrar_animals(list_animals):
    list_prohibidos = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda animal: animal not in list_prohibidos, list_animals))

print(filtrar_animals(list_animals))

# Additional one from ex.9 - trying another function
animals2 = ["Cat", "Parrot", "Monkey", "Dog", "Spiders", "Snake", "Blue Parrot"]

def filter_animals(animals2):
    list_not_alload = ["Blue Parrot", "Monkey", "Snake", "Tiger"]
    return list(filter(lambda animals: animals not in list_not_alload,animals2))

print(filter_animals(animals2))

# 10. Escribe una función que reciba una lista de números y calcule su promedio.
# Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente

class ListaVaciaError(Exception):
    pass

def calcular_promedio(numeros):
    if len(numeros) == 0:
        raise ListaVaciaError("La lista está vacía")

    return sum(numeros) / len(numeros)

try:
    numeros = [10, 20, 30, 40]

    promedio = calcular_promedio(numeros)

    print(f"Promedio: {promedio}")

except ListaVaciaError as error:
    print(f"Error: {error}")

# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
# valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

try:
  edad = int(input("Indicate your age: "))
  
  if edad < 0 or edad > 120:
        print("Incorrect age range, indicate a valid number from 0 to 120")
  else:
    print(f"The age is {edad}")

except ValueError:
    print("Please enter a numeric value")

# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

statement = "Hola a todos"

def len_words(statement):
    words = statement.split()
    return list(map(len, words))

print(len_words(statement))

# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. 
# Las letras no pueden estar repetidas. Usa la función map()

letters = ["a", "e", "i", "o", "u"]

def convert_letters(letters):
    unique_letters = set(letters)

    return list(map(lambda letter: (letter.upper(), letter.lower()), unique_letters))

print(convert_letters(letters))

# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. 
# Usa la función filter()

lista_nombres = ["Carlos", "Cecilia", "Maria", "Pedro", "Celia", "Clodoaldo", "Joao"]

def solo_C(lista_nombres, letra="C"):
    return list(filter(lambda nombre: nombre.startswith(letra), lista_nombres))

print(solo_C(lista_nombres))

# 15. Crea una función lambda que sume 3 a cada número de una lista dada.

even_numbers = [2, 4, 6, 8, 20]

def add_plus3(even_numbers):
    return list(map(lambda n: n + 3,even_numbers))

print(add_plus3(even_numbers))

# note to check funcion in a different list

odd_numbers = [3, 5, 7, 9]
print(add_plus3(odd_numbers))

statement2 = "I am quite enjoying this module"

def len_words2(statement2, n=4):
    words = statement2.split()
    return list(filter(lambda word: len(word) > n, words))

print(len_words2(statement2))

# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. 
# Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función reduce()
# note: needed support for this one

from functools import reduce

def digits_to_number(digits):
    return reduce(lambda acc, digit: acc * 10 + digit, digits)

print(digits_to_number([5, 7, 2]))


# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes 
# (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90 - Usa la función filter()

students = [{"Name": "Charles", "Age": 44, "Qualification": 95},
            {"Name": "Susan", "Age": 43, "Qualification": 90},
            {"Name": "Giles", "Age": 33, "Qualification": 74},
            {"Name": "Sophie", "Age": 39, "Qualification": 67},
            {"Name": "Rodri", "Age": 41, "Qualification": 100}]

def qualificacion_superior(students):
    return list(filter(lambda student: student["Qualification"] >= 90,students))

print(qualificacion_superior(students))

# 19. Crea una función lambda que filtre los números impares de una lista dada.

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def filtrar_odds(lista_numeros):
    return list(filter(lambda n: n % 2 != 0, lista_numeros))

print(filtrar_odds(lista_numeros))

#additional note: check again the funcion

lista_numeros2 = [301, 300, 304, 209487, 222, 231, 642, 56, 646, 87, 889, 2000]
print(filtrar_odds(lista_numeros2))

# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. 
# Usa la función filter()

mixed_list = ["Sao Paulo", 500, "Madrid", 700, "New York", 800, "Mexico City", 250]

lista_values = list(filter(lambda value: isinstance(value, int), mixed_list))

print(lista_values)

# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda

def calculate_cube(numero):
    cube = lambda n: n ** 3
    return cube(numero)

print(calculate_cube(4))
print(calculate_cube(65))

# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .

from functools import reduce

lista_10 = [10, 100, 1000, 10000, 10000]

def total_product(lista_10):
    return reduce(lambda x, y: x * y, lista_10)

print(total_product(lista_10))

# 23. Concatena una lista de palabras.Usa la función reduce().

from functools import reduce

lista_palavras = ["Get", "ready", "with", "me"]

def concatenar(lista):
    return reduce(lambda x, y: x + " " + y, lista)

print(concatenar(lista_palavras))

# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().

lista_20 = [80, 40, 20]

def diferencia_total(numeros):
    return reduce(lambda x, y: x - y, numeros)

print(diferencia_total(lista_20))


# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

text1 = "You can do it !"

def count_letters(text):
    return len(text)

print(count_letters(text1))

# additional note: trying fuction with another string

text2 = "You can always count on me"
print(count_letters(text2))
    
# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

numero1 = 30
numero2 = 25

calculate_divison = lambda x, y: x % y

print(calculate_divison(numero1,numero2))

# 27. Crea una función que calcule el promedio de una lista de números

lista30 = [1, 5, 15, 11, 12, 30]

def promedio(lista):
    return round(sum(lista) / len(lista), 2)

print(promedio(lista30))

# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

lista_regions = ["AMEA", "LA", "NA", "LA", "MEU"]

def first_duplicated(lista):
    duplicates = set()

    for elemento in lista:
        if elemento in duplicates:
            return elemento
        duplicates.add(elemento)

    return None

print(first_duplicated(lista_regions))

# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#',
#  excepto los últimos cuatro.
# note: needed help with this one 

def enmascarar(value):
    text = str(value)

    return "#" * (len(text) - 4) + text[-4:]

print(enmascarar(569847521254))

# 30. Crea una función que determine si dos palabras son anagramas, es decir, 
# si están formadas por las mismas letras pero en diferente orden

word1 = "pata"
word2 = "tapa"

def son_anagramas(w1, w2):
    return sorted(w1) == sorted(w2)

print(son_anagramas(word1, word2))

# note: check function with another word

word3 = "patas"

print(son_anagramas(word3,word2))

# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
# esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.
#note: I am not sure about this one

def buscar_nombre():
    nombres = input("Introduce una lista de nombres separados por comas: ")
    lista_nombres = [n.strip() for n in nombres.split(",")]

    nombre_buscar = input("Introduce el nombre a buscar: ")

    if nombre_buscar in lista_nombres:
        print("El nombre fue encontrado en la lista.")
    else:
        raise Exception("El nombre no está en la lista")


# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
# devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

employees = [
    {"name": "Cecilia Menicucci", "role": "Developer"},
    {"name": "Ana Garcia", "role": "Designer"},
    {"name": "Alexandra Hillton", "role": "Manager"}
]

def find_employee(full_name, employee):
    for employee in employees:
        if employee["name"] == full_name:
            return employee["role"]

    return "This person no longer works here"

print(find_employee("Cecilia Menicucci",employees))
print(find_employee("Alvaro Solana",employees))

# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas

lista1 = [100, 250, 341]
lista2 = [445, 55, 623]

suma_listas = lambda l1, l2: list(map(lambda x, y: x + y, l1, l2))

print(suma_listas(lista1, lista2))

# 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: 
# crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
# manipular la estructura del árbol.
# Código a seguir:
# - Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
# - Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
# - Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
# - Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
# - Implementar el método quitar_rama para eliminar una rama en una posición específica.
# - Implementar el método 
# info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las
# mismas.
# 
# Caso de uso:
# - Crear un árbol.
# - Hacer crecer el tronco del árbol una unidad.
# - Añadir una nueva rama al árbol.
# - Hacer crecer todas las ramas del árbol una unidad.
# - Añadir dos nuevas ramas al árbol.
# - Retirar la rama situada en la posición 2.
# - Obtener información sobre el árbol.

# support needed for this one 

class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print("Posición inválida")

    def info_arbol(self):
        return {
            "tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }

# 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
# corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
# agregar dinero al saldo.
# Código a seguir:
# - Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
# - Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no
# poder hacerse.
# - Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual.
# Lanzará un error en caso de no poder hacerse.
# - Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
# 
# Caso de uso:
# - Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
# - Agregar 20 unidades de saldo de "Bob".
# - Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
# - Retirar 50 unidades de saldo a "Alicia"

# note: support needed for this one 

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def agregar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0")

        self.saldo += cantidad
        print(f"{self.nombre} ahora tiene {self.saldo}")

    def retirar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0")

        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente")

        self.saldo -= cantidad
        print(f"{self.nombre} ahora tiene {self.saldo}")

    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0")

        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente para transferir")

        self.saldo -= cantidad
        otro_usuario.saldo += cantidad

        print(f"Transferencia realizada: {cantidad} de {self.nombre} a {otro_usuario.nombre}")

# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras , 
# reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
# de la función procesar_texto .
# Código a seguir:
# - Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene
# que devolver un diccionario.
# - Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene
# que devolver el texto con el remplazo de palabras.
# - Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra
# eliminada.
# - Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un
# número de argumentos variable según la opción indicada.
# Caso de uso:
# Comprueba el funcionamiento completo de la función procesar_texto

# note: suport needed for this one

def procesar_texto(texto, opcion, *args):

    if opcion == "contar":
        return contar_palabras(texto)

    elif opcion == "reemplazar":
        palabra_original, palabra_nueva = args
        return reemplazar_palabras(texto, palabra_original, palabra_nueva)

    elif opcion == "eliminar":
        palabra = args[0]
        return eliminar_palabra(texto, palabra)

    else:
        return "Opción no válida"


#38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

horario = float(input("Que hora es? Ingrese de 0-23"))
print(horario)

if horario > 5.0 and horario <= 12.0:
    print("Es día")
elif horario > 12.0 and horario <= 18.0:
    print("Es tarde")
else:
    print("Es noche")

#39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
# # Las reglas de calificación son:
# - 0 - 69 insuficiente
# - 70 - 79 bien
# - 80 - 89 muy bien
# - 90 - 100 excelente

calificacion = int(input("Indicar la calificacion numerica"))
print(calificacion)

if calificacion >= 90 :
    print(f"Excelente")
elif calificacion >=80 and calificacion <90:
    print("Muy bien")
elif calificacion >=70 and calificacion <80:
    print(f"Bien")
else:
    print(f"Insuficiente")

# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o 
# "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).

import math

def calcular_area(figura, datos):

    if figura == "rectangulo":
        base, altura = datos
        return base * altura

    elif figura == "circulo":
        radio = datos[0]
        return math.pi * radio ** 2

    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2

    else:
        return "Figura no válida"
    
    # note: support needed for this exercice.

# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo
# siguiente:
# - Solicita al usuario que ingrese el precio original de un artículo.
# - Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
# - Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
# - Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayora cero). Por ejemplo, descuento de 15€. 
# - Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 
# - Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python.


precio_original = float(input("Introduce el precio original del artículo: "))
cupon = input("¿Tienes un cupón de descuento? (si/no): ").lower()
descuento = 0

if cupon == "si":
    valor_cupon = float(input("Introduce el valor del cupón: "))

    if valor_cupon > 0:
        descuento = valor_cupon
    else:
        print("Cupón inválido, no se aplicará descuento.")

elif cupon == "no":
    print("No se aplicará ningún descuento.")

else:
    print("Respuesta no válida, se asumirá sin descuento.")

precio_final = precio_original - descuento

# Evitar precios negativos
if precio_final < 0:
    precio_final = 0

print(f"Precio final de la compra: {precio_final}")


