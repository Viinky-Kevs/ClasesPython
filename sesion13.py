#Actividad 1
#
#Vamos a escribir una funcion que llene una matriz de 5 filas y 10 columnas con números enteros entre 1 y 100
#aleatorios, imprima los valores máximo y mínimo y sus posiciones dentro de la matriz.

def actividad1():
    print("Actividad 1")
    from numpy import random as rd
    import numpy as np
    
    matriz =[[],[],[],[],[]]
    
    while len(matriz[4]) < 10:
        ran_num = rd.randint(1,100)
        
        if len(matriz[0]) < 10:
            matriz[0].append(ran_num)
        elif len(matriz[1]) < 10:
            matriz[1].append(ran_num)
        elif len(matriz[2]) < 10:
            matriz[2].append(ran_num)
        elif len(matriz[3]) < 10:
            matriz[3].append(ran_num)
        elif len(matriz[4]) < 10:
            matriz[4].append(ran_num)
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=' ')
        print()
    
    mini = []
    
    for i in matriz:
        for j in i:
            mini.append(j)
    
    minimo = np.argmin(mini)
    maximo = np.argmax(mini)
    
    print("El número menor de la matriz es:",mini[minimo])
    print("El número mayor de la matriz es:",mini[maximo])
    #print(mini)
    
    num_min = []
    num_max = []
    for i in matriz:
        n_minimo = np.argmin(i)
        n_maximo = np.argmax(i)
        num_min.append(n_minimo)
        num_max.append(n_maximo)
    
    lista_num1 = []
    counter = 0
    for i in num_min:
        valores = matriz[counter][i]
        counter += 1
        lista_num1.append(valores)
    
    valor_min = np.argmin(lista_num1)
    
    print(f"El valor mínimo se encuentra en: [{valor_min},{num_min[valor_min]}]")
    
    lista_num2 = []
    counter = 0
    for i in num_max:
        valores = matriz[counter][i]
        counter += 1
        lista_num2.append(valores)
    
    valor_max = np.argmax(lista_num2)
    print(f"El valor máximo se encuentra en: [{valor_max},{num_max[valor_max]}]")
    
#Actividad 2
#
#El producto escalar de un número real, x , y una matriz A es la matriz xA. 
#Cada elemento de la matriz xA es x veces su elemento correspondiente en A.
#
#Diseñemos una funcion escalar(matriz, escalar) que dada matriz[n][m] y un escalar, 
#imprima el producto escalar de la matriz.

def actividad2():
    print("Actividad 2")
    m,n = input("Escriba la dimensión de la matriz: ").split("x")
    ask= str(input("¿Quiere que los números sean aleatorios?[S/N]: ").upper())
    
    m = int(m)
    n = int(n)
    
    matriz = []
    for i in range(m*n):
        matriz.append([])
    
    if ask == "N":
        print(f"Escriba los {m*n} números de la matriz separados por coma")
        numbers = input("Números de la matriz: ").split(",")
        for i in numbers:
            
    
    
    x = float(input("Escriba el número para hallar el escalar: "))
    
    matriz_escalar = []
    
    for i in range(len(matriz)):
        matriz_escalar.append([])
    
    for i in matriz:
        for j in i:
            escalar = j*x
            matriz_escalar[i].append(escalar)
            
    for i in range(len(matriz_escalar)):
        for j in range(len(matriz_escalar[i])):
            print(matriz_escalar[i][j], end=' ')
        print()

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
                actividad1()
            elif option == 2:
                actividad2()
            else:
                print("La opción no es valida")
















