""" Utilizamos la función input() para solicitar al usuario que ingrese la longitud de los lados del triángulo, los cuales se almacenan en las variables a, b y c.

A continuación, se evalúa el valor de las variables a, b y c utilizando estructuras if y se determina si el triángulo es equilátero, isósceles, rectángulo o escaleno.

Si los tres lados son iguales, entonces el triángulo es equilátero. Si dos de los lados son iguales, entonces el triángulo es isósceles. Si la suma de los cuadrados de dos de los lados es igual al cuadrado del tercer lado, entonces el triángulo es rectángulo. En cualquier otro caso, el triángulo es escaleno. """


a = float(input("Ingrese la longitud del lado A: "))
b = float(input("Ingrese la longitud del lado B: "))
c = float(input("Ingrese la longitud del lado C: "))

if a == b and b == c:
    print("El triángulo es equilátero")
elif a == b or b == c or a == c:
    print("El triángulo es isósceles")
elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
    print("El triángulo es rectángulo")
else:
    print("El triángulo es escaleno")