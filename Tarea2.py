import threading
from itertools import chain
import time 
import argparse

## Se configuran los argumentos
## que se utilizaran en el programa para ser
## introducidos por medio de una consola de texto
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--array" , type=int, help="Tamaño del array")
parser.add_argument("-s", "--save" , type=int, help="Decide si desea guardar los tiempos o no")
arg = parser.parse_args()

## Función encargada de generar una lista con los valores
## desde 0 hasta X-1
def Array(X):
    Output = []
    for i in range(X):
        Output.append(i)
    return Output

## Función encargada de recorrer una lista y
## elevar el valor de cada elemento al cuadrado,
## además incluye un retardo para evidenciar el
## aumento de velocidad con 4 hilos
def Potencia (Array):
    for i in range(len(Array)):
        Array[i]=Array[i]**2
        time.sleep(0.00005)
    return Array

## Función encargada de tomar un array y
## partirla en una cantidad variable de partes
## al crear un ciclo que va desde el índice cero
## y aumenta por una n-ésima parte de la
## longitud del array para avanzar a la
## siguiente parte hasta recorrerlo todo
def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out

## Función que crea un array con X elementos distintos,
## seguidamente eleva al cuadrado cada uno de estos elementos
## Este procedimiento se realiza con 1 hilo y
## luego con 4 hilos
## Se mide el tiempo tomado con ambos métodos
## para ser comparados
## Además, toma el argumento save que determina si
## los resultados de tiempo serán guardados en
## un archivo de texto (save=1) o si los resultados
## serán presentados en pantalla (save=0),
## en caso de no introducir el argumento save,
## se imprimiran los resultados en pantalla (save=0)
def Hilos (X, save):

    ##Caso para un hilo
    s1=Array(X)

    ## Se crea un hilo que ejecutará
    ## la función Potencia con el argumento s1
    t1 = threading.Thread(target=Potencia, args=(s1,))

    ## Se mide el tiempo de inicio
    ## y se inicia al hilo
    start1=time.time()
    t1.start()

    ## Se espera a que el hilo termine su
    ## ejecución y se mide el tiempo
    t1.join()
    end1=time.time()
    
    ##print(s)
    ##print("1 thread execution is complete!")

    ##Caso para 4 hilos
    s4=Array(X)
    ss=chunkIt(s4,4)

    ## Se crea 4 hilos que ejecutarán
    ## la función Potencia, cada hilo
    ## utilzará una cuarta parte del array
    t1 = threading.Thread(target=Potencia, args=(ss[0],))
    t2 = threading.Thread(target=Potencia, args=(ss[1],))
    t3 = threading.Thread(target=Potencia, args=(ss[2],))
    t4 = threading.Thread(target=Potencia, args=(ss[3],))

    ## Se mide el tiempo de inicio
    ## y se inician los hilos
    start4=time.time()
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    ## Se espera a que los hilos terminen su
    ## ejecución y se mide el tiempo
    t1.join()
    t2.join()
    t3.join()
    t4.join()

    end4=time.time()

    ##print(list(chain(*ss)))
    ##print("4 threads execution is complete!")

    ## Si save es 1, se guardan los datos en un .txt
    ## Si save es 0, los resultados se imprimen en pantalla
    if save == 1:
        file = open("tiempos.txt", "w")
        file.write("Execution time with 1 thread:" + repr(end1-start1) + "\n")
        file.write("Execution time with 4 threads:" + repr(end4-start4) + "\n")
        file.close

    else:
        print("Execution time with 1 thread:", end1-start1)
        print("Execution time with 4 threads:", end4-start4)
   
## Llamado a función principal con los
## argumentos introducidos en la consola de texto
Hilos(arg.array, arg.save)


