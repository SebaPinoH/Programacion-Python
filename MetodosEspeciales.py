#el metodo def __del__,  es un metodo destructor cuando finaliza todo el pusle del objecto, se ejecuta el destrucctor y elimina todo lo creado tanto en memoria como en la funcion.

class FabricaTelefono():
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

        print ("El objecto {} ha sido creado".format(self.marca))
    
#clase por defecto de python para poder entender este tipo de mensaje <__main__.FabricaTelefono object at 0x104c84a90>
    def __str__(self):
        return "El objecto {} ".format(self.marca)

    def __del__(self):
        print("El objecto {} ha sido destruido".format(self.marca))


telefono = FabricaTelefono("Nokia","Negro")

print(telefono.marca)
print(telefono)