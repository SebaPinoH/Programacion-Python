class A():
    def __init__(self):
        self._contador = 0
        self._cuenta = 0

    #esta es el metodo GET para poder llamar el metodo GET como un atributo
    @property
    def cuenta(self):
        return self._cuenta
    
    #Metodo SET
    @cuenta.setter
    def cuenta(self, cuenta):
        self._cuenta = cuenta

    #METODO GET
    @property
    def contador(self):
        return self._contador

    #METODO SET
    @contador.setter
    def contador(self, contador):
        self._contador = contador

print("Obejto Encapsulado")
a = A()
print(a.cuenta)
print(a.contador)
#llamar el metodo SET
a.cuenta = 20
print(a.cuenta)
a.contador = 10
print(a.contador)
