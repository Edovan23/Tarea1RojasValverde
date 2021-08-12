import math  # Librería de operaciones matemáticas


def multiple_op(x):  # Definición de la funcion multiple_op,
    # que se encarga de realizar operaciones según su parametro de entrada
    if isinstance(x, int):  # Compara el tipo de variable de la
        # entrada con un integer
        if x < 0:  # Compara si x es menor que 0,
            # es decir un número negativo.
            output = 2  # Error: La entrada debe ser positiva
        else:  # En caso de que el número sea valido (integer positivo)
            # realiza las operaciones usando el parámetro de entrada
            output = []  # La salida corresponde a un arreglo
            output.append(x*x)  # Agrega en el primer indice del arreglo
            # el resultado de la primera operación
            output.append(2**x)  # Agrega en el subsecuente indice del arreglo
            # el resultado de la segunda operación
            output.append(math.factorial(x))  # Agrega en el subsecuente
            # indice del arreglo el resultado de la segunda operación
    else:
        # Si el parámetro no es un número, no se puede efectuar ninguna
        # operación sobre este
        output = 1  # Error: La entrada debe ser un número
    return output


def verify_array_op(y):  # Definición de la verify_array_op, que se encarga
    # de realizar operaciones a sus arreglos de entrada, y retorna una matriz
    x = 0  # Variable de control, permite identificar si los parámetros de
    # entrada cumplen con todos los requerimientos para ser operados
    output1 = []  # La salida corresponde a un arreglo.
    for i in y:  # Ciclo for que recorre los valores del parámetro
        # de entrada y revisa si son enteros
        if type(i) != int:  # Compara el el tipo de dato del valor
            # de cada arreglo con el tipo de dato int
            x = 1  # En caso de que algun valor no sea int
            # la variable de control cambia su valor a 1
            break  # Sale del ciclo for
    if x == 0:  # Revisa si la variable de control sigue teniendo
        # un valor de 0, es decir, que no ha encontrado ningún error
        for i in y:  # Ciclo for que recorre los valores del parámetro de
            # entrada y revisa si son números positivos
            if i < 0:  # Compara cada valor de cada arreglo para identificar
                # los números negativos, si los hay
                x = 2  # En caso de que algún número es negativo, cambia la
                # variable de control al valor de 2
                break  # Sale del ciclo for
    if x == 0:  # Si no se ha encontrado ningun error la función realiza
        # su operacion sobre los parámetros de entrada
        for i in y:  # Ciclo for que recorre cada valor del arreglo de entrada
            output1.append(multiple_op(i))  # Llama la función multiple_op y
            # le envía como parametro el valor de entrada
            # Asigna en su primer índice el resultado de la función multiple_op
        return output1  # Retorna una matriz
    else:  # Si se encontró un error identifica el valor de la variable de
        # control para determinar el problema
        if x == 1:
            return 3  # Error: Los elementos de la entrada debe ser un número
        if x == 2:
            return 4  # Error: Los elementos de la entrada debe ser positiva
