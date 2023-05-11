class A():
    def __init__(self):
        self.contador = 0

    def incrementar(self):
        self.contador += 1

    def cuenta(self):
        return self.contador


class B():
    def __init__(self):
        self.__contador = 0

    def incrementar(self):
        self.__contador += 1

    def cuenta(self):
        return self.__contador
    

print("Obejto 1")

a = A()
print(a.cuenta())
a.incrementar()
print(a.cuenta())
print(a.contador)

print("Obejto 2")

b = B()
print(b.cuenta())
b.incrementar()
print(b.cuenta())
#Esto es encapsulamiento por eso es el error, ya que no se puede acceder por fuerea de la clase de donde nacio, es una mala practica en cual era mandar de esta manera los atributos
print(b.__contador)

#RECORDAR
#Encapsular es solo para los atributos, ahora bien hay ciertas reglas que se deben respertar y seguir para poder lograr un buen encapsulamiento
#Reutimializamos la clase anterior pero con las variables encapsulada
#El _ dira que es encapsulado, en cual la mejor manera de llamar es utilizando los metodos de GET y SET, mirar el ejemplo MetoroGET.py


class A():
    def __init__(self):
        self._contador = 0
        self._cuenta = 0

    def incrementar(self):
        self._contador += 1

    def cuenta(self):
        return self._contador

print("Obejto Encapsulado")

a = A()
#esta es una manera incorrecta de llamar. utilizar los metodos de GET y SET
print(a._cuenta())
a._cuenta = 20
print(a._cuenta())