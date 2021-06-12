def actividad1():
    print("actividad1")
    # Vamos a realizar un algoritmo que nos calcule la serie de Fibonacci.
    # La serie o secuencia de Fibonacci comienza con los números 0 y 1 y 1, y a partir de allí es posible calcular el siguiente valor como la suma de los dos valores anteriores. 
    # Por ejemplo, 1+1=2, 1+2=3, 2+3=5, etc. Así, los primeros números de la secuencia son: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    # Creemos un programa que a partir de un número N ingresado, imprima los primeros N números de la serie de Fibonacci.
    number = int(input("Digite un número: "))

    lista = [0,1]

    for i in range(number):
      k = lista[i] + lista[i+1]
      lista.append(k)
    
    print(lista)
    
 
#actividad1()

def actividad2():
    print("actividad2")
    #Escribe el código usando break que reciba una palabra e imprima el número de letras que tiene y las letras hasta que, o bien termine la palabra o encuentre la letra a. .
    word = str(input("Escriba una palabra: "))

    length = len(word)
    letter = []
    
    for i in range(length):
      if word[i] != "a":
        #print(word[i])
        letter.append(word[i])
        #counter = i + 1
      else:
        break
    print(letter)
    print(f"Número total de letras: {len(letter)}")
    
#actividad2()

def actividad3():
    print("actividad3")
    #Escribe un algoritmo que lea 10 números e imprima cuantos son positivos, cuantos negativos y cuantos neutros(0).
    lista = []

    while len(lista) < 10:
      numbers = float(input("Escriba los números: "))
      lista.append(numbers)
    
    positive = []
    negative = []
    neutre = []
    
    for i in lista:
      if i < 0:
        negative.append(i)
      elif i > 0:
        positive.append(i)
      else:
        neutre.append(i)
    
    print(f"Total positivos: {len(positive)}")
    print(f"Total negativos: {len(negative)}")
    print(f"Total neutros: {len(neutre)}")
#actividad3()

def actividad4():
    print("actividad4")
    #Usando tanto while como for, escribe el codigo que pida números al usuario hasta que este ingrese -1 y que retorne el factorial de cada número ingresado usando un ciclo Para (For).
    lista = []
    entrada = None
    
    while entrada != -1:
      entrada = int(input("Escriba los números: "))
      if entrada != -1:
        lista.append(entrada)
    
    for i in lista:
      factorial = 1
      for j in range(1, i+1):
        factorial = factorial * j
      print(i, factorial)
#actividad4()


if __name__ == "__main__":
    option = int(input("Escriba una opción: "))
    
    if option == 1:
        actividad1()
    elif option == 2:
        actividad2()
    if option == 3:
        actividad3()
    if option == 4:
        actividad4()
    else:
        print("La opción no es valida")
        
        