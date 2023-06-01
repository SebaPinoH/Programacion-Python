#Se creara un diccionario de Paises, en cual uno ingresara un pais y este mostrara la capital

diccionario = {"Guatemala": "Cuidad de Guatemala", "Honduras": "Tegucigalpa","Nicaragua": "Managua", "Costa Rica": "San jose", "Panama": "Panama", "Argentina": "Buenoas Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

pais = input("Ingrese pais para conocer su Capital: ")
capital = pais.capitalize() in diccionario

if capital == True:
    print(diccionario[pais.capitalize()])
else:
    print("El pais no se encuentra en el Diccionario")