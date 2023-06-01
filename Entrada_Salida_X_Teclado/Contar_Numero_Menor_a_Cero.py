""" Utilizamos la función input() para solicitar al usuario que ingrese tres números por teclado, los cuales se almacenan en las variables numero1, numero2 y numero3. Luego, se inicializa la variable contador en cero.

A continuación, se evalúa cada número con una estructura if y se comprueba si es menor que cero. Si se cumple esta condición, se incrementa la variable contador.

Por último, se imprime un mensaje que indica cuántos de los números ingresados son menores a cero utilizando la variable contador. """

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

contador = 0

if numero1 < 0:
    contador += 1

if numero2 < 0:
    contador += 1

if numero3 < 0:
    contador += 1

print("Hay", contador, "números menores a cero")