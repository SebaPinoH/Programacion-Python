#Variables 

string_variable = "My string variable"
print(string_variable)

#Variable int
int_variable = 5
print(int_variable)

#Varible Boolean
boolean_variable = True
print(boolean_variable)

#concatenacion de variables en un print
print(string_variable,int_variable,boolean_variable)

#Convertir INT en un String
variable_cambiada = str(int_variable)
print(variable_cambiada)
print("Este es el valor de la variable cambiada a string",type(variable_cambiada))


#algunas funciones del Sistema, como contar total del string
print(len(string_variable))

#Variables en una sola linea !CUIDADO CON ABUSAR DE ESTA SINTAXIS!
nombre, apellido, edad = "Sebastian","Pino",34
print("Mi nombre es:" ,nombre,apellido, ". y mi edad es de:",edad)


#INPUT, LLENAR CAMPOS
ingresar_nombre = input("Cual es tu nombre?")
ingresar_edad = input("Cual es tu edad?")

print(ingresar_nombre)
print(ingresar_edad)
