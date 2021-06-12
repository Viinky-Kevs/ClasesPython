"""
Funciones

La verdad es que hemos venido trabajando con funciones desde que empezamos con archivos .py 
En Python, definimos una función con la siguiente estructura

def funcion(parametros)

Recuerda que los parametros son opcionales!
"""

def suma(a,b):
    
    print(a+b)

#suma(3,4)


#Actividad 1
#Usted es cajero en un supermercado de su ciudad. Su trabajo es imprimir cada uno de los productos de su cliente, su precio y calcular el total a pagar.
#
#Diseña un programa con las siguiente características:
#
#    1. Que tenga una función caja que solicite al usuario nombre y precio de cada producto.
#    2. Una variable total que vaya sumando el precio de los artículos
#    3. Una función adicional llamada imprimaProducto(nombre, precio) que reciba el nombre y
#        el precio de cada producto y los imprima.
#    4. Que después de llamar a imprimaProducto le pregunte al usuario si tiene o no más artículos a ingresar. Si no tiene, el programa debe detenerse.
#    5. Si no hay más artículos, que imprima el total de la compra

#    Al final de tus funciones, puedes simplement llamar a la función caja para probar


def caja():
    precios = []
    nombres = []
    nombre_1 = "inicio"
    while nombre_1 != "imprimaProducto":
        nombre_1 = str(input("Ingrese el nombre del producto: "))
        if nombre_1 == "imprimaProducto":
            def imprimaProducto():
                for i in range(len(nombres)):
                    print(nombres[i],"= $",precios[i])
            articulos = str(input("Tiene más artículos para ingresar [S/N]: ").upper())
            
            if articulos == "S":
                nombre_1 = "inicio"
            elif articulos == "N":
                break
            else:
                print("No se reconoce comando")
                nombre_1 = "inicio"
            
        else:
            #nombre_1 = str(input("Ingrese el nombre del producto: "))
            precio_1 = float(input("Ingrese el precio del producto: "))
            nombres.append(nombre_1)
            precios.append(precio_1)
               
    imprimaProducto()
    print("Total: $",sum(precios))
    
#caja()

#Actividad 2
#
#Escribamos una función numAleatorio() que retorne un número aleatorio entre 100 y 130, 
#excepto los números 110, 115 y 120 .
#
#Adicionalmente, una función numeros que imprima diez números aleatorios 
#(retornados por la función numAleatorio()) alternando par, impar, comenzando por par.


def numeros():
    import numpy as np
    
    for i in range(1):
        numbers = np.random.randint(100, 130)
        if numbers != 110 and numbers != 115 and numbers != 120:
            continue
    print(numbers)
        
#diez()

#numeros()

if __name__ == "__main__":
    option = int(input("Ingrese una opción [1,2]: "))
    
    if option == 1:
        caja()
    elif option == 2:
        numeros()
    else:
        print("opción no valida")












































