num = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))

for i in range(1, 11):
    resultado = num * i
    print(num, "x", i, "=", resultado)