"""     Se utiliza la función input() para solicitar al usuario que ingrese un número. La función input() devuelve una cadena de texto, por lo que es necesario convertir el valor ingresado a un número entero utilizando la función int().
    Se utiliza una estructura if-else para verificar si el número ingresado es mayor o igual a 2 y menor o igual a 100. Si el número es menor a 2 o mayor a 100, se muestra un mensaje indicando que el número ingresado no es válido.
    Dentro de la estructura if-else, se utiliza otra estructura if-else para verificar si el número ingresado es par o impar. Si el número es divisible entre 2 (es decir, su resto al dividirlo por 2 es 0), se considera que es un número par y se muestra un mensaje correspondiente. En caso contrario, se considera que es un número impar y se muestra un mensaje correspondiente. """

num = int(input("Ingrese un número entre 2 y 100: "))

if num < 2 or num > 100:
    print("El número ingresado no es válido.")
else:
    if num % 2 == 0:
        print("El número ingresado es par.")
    else:
        print("El número ingresado es impar.")
