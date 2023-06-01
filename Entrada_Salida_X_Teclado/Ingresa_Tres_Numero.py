""" Utilizamos la función input() para solicitar al usuario que ingrese tres números por teclado, los cuales se almacenan en las variables numero1, numero2 y numero3. Luego, se inicializan las variables suma y contador en cero.

A continuación, se evalúa cada número con una estructura if y se comprueba si es mayor que cero y si es par utilizando el operador módulo %. Si cumple ambas condiciones, se suma a la variable suma, de lo contrario, se incrementa la variable contador.

Por último, se evalúa si la variable contador es igual a tres, lo que significa que no se ingresaron números positivos y/o pares. En ese caso, se imprime un mensaje indicando que no se cumplieron las condiciones. De lo contrario, se imprime la suma de los números positivos y pares utilizando la variable suma. """


numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

suma = 0
contador = 0

if numero1 > 0 and numero1 % 2 == 0:
    suma += numero1
else:
    contador += 1

if numero2 > 0 and numero2 % 2 == 0:
    suma += numero2
else:
    contador += 1

if numero3 > 0 and numero3 % 2 == 0:
    suma += numero3
else:
    contador += 1

if contador == 3:
    print("No se ingresaron números positivos y/o pares")
else:
    print("La suma de los números positivos y pares es:", suma)