"""
Mientras Que

Como vimos anteriormente, en Python, el ciclo Mientras Que se maneja con "while". 

Por ejemplo:
"""

def ejemplo1():
    i = 1
    while i < 6:
        print(i)
        i += 1
#ejemplo1()

def actividad1():
    print("actividad1")
    # Continuemos integrando los conceptos que hemos visto hasta el momento. 
    # Ahora vamos a elaborar un algoritmo que pida un número al usuario, e imprima todos los números pares desde 2 hasta el número. 
    number = int(input("Ingrese un número"))
    i = 2
    while i <= number:
        print(i)
        i += 2
# Para ejecutar cada actividad, debes quitar el comentario a la línea que llama el bloque de código
#actividad1()

def actividad2():
    print("actividad2")
    #Escribe el código un ciclo para obtener el número de dígitos de un número ingresado por el usuario.
    num1 = int(input("Ingrese el numero: "))
    digito = 1
    while num1 > 0:
        num1 = num1//10
        digito += 1
        if num1 == 1:
            print(digito)
actividad2()    
    

def actividad3():
    import numpy as np
    print("actividad3")
    #Escribe el código que solicite números al usuario hasta que éste ingrese -1.
    #Cuando se ingrese -1, el programa debe imprimir el promedio de todos los números ingresados hasta ese momento (sin contar con el -1).
    numbers = None
    dicti = []
    
    while numbers != -1:
        numbers = int(input("Ingrese números (para terminar digite -1): "))
        if numbers != -1:
            dicti.append(numbers)
    media = np.mean(dicti)        
    print(f"El promedio de {dicti} es {media}")
    
#actividad3()