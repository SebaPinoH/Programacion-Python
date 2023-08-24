#Esta es una clase llamada Estudiantem con atributos de nombre y nota
#Definiremos los metodos de iniciarlizar sus atributos, imprimir, y mostrar mensaje aprobado o no por pantalla.

class Estudiante():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre: {} \n Nota: {}".format(self.nombre, self.nota))

    def resultado(self):
        if self.nota < 7:
            print("Has Reprobado!")
        else:
            print("Has Aprobado!")

estudiante1 = Estudiante('Sebastian', 10)
estudiante1.imprimir()
estudiante1.resultado()