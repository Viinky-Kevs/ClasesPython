"""
Matrices o vectores bidimensionales

Vamos a utilizar esta sesión para repasar los conceptos vistos y a aprender otras funciones interesantes 
en Python.

La función string.split(), por ejemplo, toma una cadena de caracteres (string) y la pasa a una lista.
Por defecto el separador es cada espacio en blanco, pero se puede seleccionar cualquier separador. 
Veamos un ejemplo:
"""
def ejemplo1(frase):
    lista = frase.split()
    print(lista)

#ejemplo1("Esta es una prueba para pasar a una lista")

#Actividad 1
#
#Escribe una función actividad1(x, n) que reciba una frase x y un numero entero n 
#e imprima una lista con las palabras cuya longitud sea mayor a n de entrada.

def actividad1(frase, n):
    palabras = frase.split()
    palabra = []
    for i in palabras:
        if len(i) >= n:
            palabra.append(i)
        else:
            continue
    print(f"Las palabras con longitud mayor a {n} son: {palabra}")
#actividad1("Esta es una prueba para pasar a una lista",3)

#Actividad 2
#
#Creemos ahora una función crearMatriz(m,n) que genere una matriz de M * N con números aleatorios 
#entre 0 y 9 y la retorne.
#
#Creemos también una función calcularPromedio(T) que dada una matriz T, genere un promedio de todos 
#sus elementos y lo retorne.
#
#Finalmente una función actividad2(m,n) que llame a crearMatriz, pase esa matriz a calcularPromedio(T) 
#y que genere una matriz que tenga el valor 1 en aquellas posiciones donde el valor sea mayor o igual 
#al promedio en T y cero (0) donde el valor de la posición en T sea menor que el promedio.
#
#Imprimir ambas matrices.

def actividad2():
    row,column = input("Escriba la dimensión de la matriz: ").split("x")
    n = int(row)
    m = int(column)
    
    def crearMatriz(n,m):
        import numpy as np
        
        matriz = []
        
        m = int(m)
        
        for i in range(n):
            matriz.append([])
        
        cant_row = len(matriz)
        
        while len(matriz[cant_row-1]) < m:
            for i in matriz:
                for j in range(len(matriz)):
                    ran_num = np.random.randint(0,9)
                    if len(i) < m:
                        matriz[j].append(ran_num)
                    else:
                        continue
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                print(matriz[i][j], end=' ')
            print()
        
        def calcularPromedio(T):
            import numpy as np
            
            matriz_1 = []
            
            for i in T:
                for j in i:
                    matriz_1.append(j)
            prom = np.mean(matriz_1)
            return(prom)
        
        calcularPromedio(matriz)
        
        matriz_final = []
        for i in range(n):
            matriz_final.append([])
        
        promedio = calcularPromedio(matriz)
        
        matriz_2 = []
        for i in matriz:
            for j in i:
                if j >= promedio:
                    matriz_2.append(1)
                else:
                    matriz_2.append(0)
        
        while len(matriz_final[cant_row - 1]) < m:
            for i in matriz_2:
                for j in range(len(matriz_final)):
                    if len(matriz_final[j]) < m:
                        matriz_final[j].append(i)
        
        print(matriz_final)
        print(matriz_2)
    
    crearMatriz(n, m)

## Inicio de selección de opción para seleccionar las actividades

if __name__ == "__main__":
    
    option = "Inicio"
    
    finish = ["Terminé", "Hecho","terminé", "hecho","Finalizado","finalizado"]
    
    while option not in finish:
        option = str(input("Ingrese una opción: "))
        if option in finish:
            break
        else:
            option = int(option)
            if option == 1:
                actividad1("Esta es una prueba para pasar a una lista",3)
            elif option == 2:
                actividad2()
            else:
                print("La opción no es valida")