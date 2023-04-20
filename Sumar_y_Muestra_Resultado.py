"""     Se utiliza la función input() para solicitar al usuario que ingrese dos números. La función input() devuelve una cadena de texto, por lo que es necesario convertir los valores ingresados a números enteros utilizando la función int().
    Los números ingresados se suman y se guarda el resultado en la variable resultado.
    Finalmente, se utiliza la función print() para mostrar el resultado por pantalla. Se utiliza la concatenación de cadenas de texto y la coma para separar el mensaje del valor que se desea mostrar. """

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

resultado = num1 + num2

print("El resultado de la suma es:", resultado)