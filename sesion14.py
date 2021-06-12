"""
Matrices o vectores bidimensionales

Vamos a continuar con el trabajo de matrices usando lista de listas. 
Como vimos en la sesión anterior, las operaciones de este tipo de matrices se pueden realizar con ciclos anidados.
"""

#Actividad 1

#Escribe una función actividad1(x) que imprima la diagonal principal de una matriz x. 
#Asegúrate de validar si la matriz es cuadrada, sino devuelve un mensaje, "La matriz no es cuadrada"

def actividad1(matriz):
    
    print("Actividad 1")
    
    p_v = matriz[0]
    
    for i in matriz:
        if len(i) != len(p_v):
            print("La matriz no es cuadrada")
            break

#actividad1([[1,1],[2,7,2],[3,3,3]])

#Actividad 2
#
#Creemos ahora una función actividad2() que reciba los elementos de una matriz 3x3 e imprima:
#
#   - La primera fila
#   - La primera columna
#   - Accede al elemento en la fila 1, columna 1.
#
#Los valores son ingresados por filas [0][1], [0][2], [0][3], [1][0], etc

def actividad2():
    print("Actividad 2")

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
                actividad1([[1,1],[2,7,2],[3,3,3]])
            elif option == 2:
                actividad2()
            else:
                print("La opción no es valida")