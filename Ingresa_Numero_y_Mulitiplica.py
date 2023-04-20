""" Se utiliza la función input() para solicitar al usuario que ingrese un número. La función input() devuelve una cadena de texto, por lo que es necesario convertir el valor ingresado a un número entero utilizando la función int(). """

num = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))

""" Se utiliza un ciclo for para recorrer los números del 1 al 10. La función range(1, 11) genera una secuencia de números del 1 al 10 (el límite superior no se incluye en la secuencia).
    Dentro del ciclo for, se calcula el resultado de la multiplicación entre el número ingresado y el número actual del ciclo, y se guarda en la variable resultado. """

for i in range(1, 11):
    resultado = num * i
    print(num, "x", i, "=", resultado)
    """ Finalmente, se utiliza la función print() para mostrar cada operación de multiplicación y su resultado por pantalla. Se utiliza la concatenación de cadenas de texto y la coma para separar los valores y mostrarlos correctamente """