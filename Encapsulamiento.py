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