# Polimorfismo: La modificacion de metodos cuando se heredan de otras clase, o que pueda apuntar al mismo metodo pero sean distintas clases


class Animales():
    def __init__(self, mensaje):
        self.mensaje = mensaje


    def hablar (self):
        print(self.mensaje)

class Perro(Animales):
    def hablar(self):
        print("Yo hablo")

class Pez(Animales):
    def hablar(self):
        print("Yo no hablo")

perro = Perro("AAAAA")
perro.hablar()