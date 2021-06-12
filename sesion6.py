# DiseÃ±ar 3 funciones:
#
#   1. Leer un nÃºmero de 4 dÃ­gitos, mostrar el dÃ­gito mayor e 
#      informar si es par o impar.
#   2. Leer dos nÃºmeros de 3 dÃ­gitos cada uno, formar un tercer nÃºmero 
#      con el mayor del primero y el menor del segundo.
#   3. Leer un nÃºmero de 3 dÃ­gitos y formar el mayor nÃºmero posible 
#      con sus cifras.
#   
# Crea la funciÃ³n principal como un menú con las tres opciones.

def funcion1():
    print("Entró a la opción 1")
    numero = int(input("Ingrese un número de 4 dígitos: "))
    numero = str(numero)
    numero = list(numero)
    numero_1 = int(numero[0])
    numero_2 = int(numero[1])
    numero_3 = int(numero[2])
    numero_4 = int(numero[3])
    lista = [numero_1, numero_2, numero_3, numero_4]
    maximo = max(lista)
    if maximo % 2 == 0:
        es_1 = "par"
    else:
        es_1 = "impar"
    print("El mayor dí­gito es: ", maximo, "y es", es_1) 

def funcion2():
    print("Entró a la opción 2")
    numero_1 = int(input("Digite un número de 3 digitos: "))
    numero_2 = int(input("Digite un número de 3 digitos: "))
    
    numero_1 = str(numero_1)
    numero_1 = list(numero_1)
    numero_1_1 = int(numero_1[0])
    numero_1_2 = int(numero_1[1])
    numero_1_3 = int(numero_1[2])
    lista = [numero_1_1, numero_1_2, numero_1_3]
    maximo = str(max(lista))
    
    numero_2 = str(numero_2)
    numero_2 = list(numero_2)
    numero_2_1 = int(numero_2[0])
    numero_2_2 = int(numero_2[1])
    numero_2_3 = int(numero_2[2])
    lista = [numero_2_1, numero_2_2, numero_2_3]
    minimo = str(min(lista))
    
    maximo += minimo
    
    print("El nuevo dí­gito es: ", maximo)

def funcion3():
    print("Entró a la opción 3")
    numero = int(input("Digite un número de 3 dígitos: "))
    numero = str(numero)
    numero = list(numero)
    numero_1 = numero[0]
    numero_2 = numero[1]
    numero_3 = numero[2]
    lista = [numero_1, numero_2, numero_3]
    lista.sort(reverse = True)
    numero_mayor = lista[0]
    numero_medio = lista[1]
    numero_menor = lista[2]
    
    numero_mayor += numero_medio
    numero_mayor += numero_menor
    print("El nuevo dí­gito es: ", numero_mayor)

if __name__ == "__main__":
    print("1. Leer un número de 4 dí­gitos, mostrar el dí­gito mayor e informar si es par o impar.")
    print("2. Leer dos números de 3 dí­gitos cada uno, formar un tercer número con el mayor del primero y el menor del segundo.")
    print("3. Leer un número de 3 dí­gitos y formar el mayor número posible con sus cifras.")    
    
    opcion = int(input("Digite una opción [1-3]: "))
    
    if opcion == 1:
        funcion1()
    elif opcion == 2:
        funcion2()
    elif opcion == 3:
        funcion3()
    else:
        print("Seleccione una opción válida")