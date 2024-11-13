# 1. Imprime "Â¡Hola Mundo!" por consola.

# 2. Escribe un comentario de una sola lÃ­nea explicando quÃ© hace el cÃ³digo del Ejercicio 1.

# 3. Imprime tu nombre y edad en la misma lÃ­nea utilizando la funciÃ³n print.

# 4. Usa la funciÃ³n type() para imprimir el tipo de dato de una cadena de texto, un nÃºmero entero y un nÃºmero decimal.

# 5. Escribe un comentario en varias lÃ­neas explicando quÃ© son los tipos de datos en Python.

# 6. Imprime el resultado de concatenar dos cadenas de texto, por ejemplo: "Hola" y "Mundo".

# 7. Crea una variable para almacenar tu nombre, otra para tu edad, e imprime ambas en la misma lÃ­nea.

# 8. Escribe un programa que solicite al usuario su nombre y lo imprima junto con un saludo.

# 9. Usa print() para mostrar el resultado de la suma de dos nÃºmeros enteros y el tipo de dato resultante.

# 10. Comenta el cÃ³digo del Ejercicio 9, y explica quÃ© hace cada lÃ­nea usando comentarios de una sola lÃ­nea.


# imprime "Hola Mundo"
print("Hola Mundo")

print("Jesús ", 43, "años")
print(type("Hola Mundo"))
print(type(5))
print(type(5.0))
'''
Los tipos de datos en Python son la representación de los diferentes datos con los que se trabaja en programación, pueden ser:
- str: cadenas de texto
- int: números enteros
- float: números decimales
- bool: Valores de verdad o falso
'''
print("hola","mundo")

a="Jesús"
b=43
print(a,b)

nombre=input("Escribe tu nombre")
edad=input("Escribe tu edad")
print(nombre,edad,"años de edad")

# Define el primer número
a=5
# define el segundo número
b=3
# realiza la suma
res = a + b
# imprime el resultado y el tipo de dato resultante
print(res, type(res))