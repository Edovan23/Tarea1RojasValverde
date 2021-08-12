from Tarea1 import multiple_op  # Importa la función multiple_op
# desde el archivo Tarea1
from Tarea1 import verify_array_op  # Importa la función verify_array_op
# desde el archivo Tarea1
import random  # Importa la libreria random para poder
# generar números aleatorios como parámetro
import math  # Importa la libreria math para poder
# calcular el factorial de un número


def test_exito_multiple_op():  # Se define un caso de éxito para
    # multiple_op con una entrada aleatoria
    a = random.randint(0, 10)  # Se genera un número entero
    # aleatorio entre 0 y 10
    assert (multiple_op(a) == [a*a, 2**a, math.factorial(a)])  # Se
    # verifica con un assert que el resultado de multiple_op sea correcto


def test_exito_verify_array_op():  # Se define un caso de éxito para
    # verify_array_op con una entrada aleatoria
    a = [0]*3  # Se crea una matriz de una fila y
    # tres columnas con valores de 0
    for i in range(3):  # Se recorren los valores desde el 0 hasta el 2
        a[i] = random.randint(0, 10)  # Se genera un número entero aleatorio
        # entre 0 y 10 y se asigna a uno de los valores de la matriz
    x0 = [a[0]*a[0], 2**a[0], math.factorial(a[0])]  # Calcula los resultados
    x1 = [a[1]*a[1], 2**a[1], math.factorial(a[1])]  # de las matrices que debe
    x2 = [a[2]*a[2], 2**a[2], math.factorial(a[2])]  # retornar verify_array_op
    assert (verify_array_op(a) == [x0, x1, x2])  # Se verifica con un assert
    # que el resultado de verify_array_op sea correcto


def test_fallo_multiple_op():  # Se define un caso de fracaso para
    # multiple_op con una entrada aleatoria
    assert multiple_op('g') == 1  # Se verifica con
    # un assert que multiple_op falle de la manera deseada
    # al introducir una letra como parámetro


def test_fallo_verify_array_op():  # Se define un caso de fracaso
    # para verify_array_op con una entrada aleatoria
    assert verify_array_op([2, 3, 'g']) == 3  # Se verifica con
    # un assert que verify_array_op falle de la manera deseada
    # al introducir una letra en un elemento del arreglo de entrada
