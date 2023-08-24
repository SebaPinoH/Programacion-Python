#Se realizara una calculadora, con 2 valores distintintos, sumando, restando, dividiendo

class Calculadura():
    def __init__(self):
        self.num1 = int(input("Ingrese el Primer Numero: "))
        self.num2 = int(input("Ingrese el Segundo Numero: "))

    def suma(self):
        self.suma = self.num1 + self.num2
        return "La suma da como resultado: ", self.suma
    
    def resta(self):
        self.resta = self.num1 - self.num2
        return "La resta da como resultado: ", self.resta
    
    def multiplicacion(self):
        self.multi = self.num1 * self.num2
        return("La multiplicacion da como resultado: "), self.multi
    
    def division(self):
        self.division = self.num1 / self.num2
        return("La division da como resiltado: "), self.division
    
calcular = Calculadura()
print(calcular.suma())
print(calcular.resta())
print(calcular.multiplicacion())
print(calcular.division())