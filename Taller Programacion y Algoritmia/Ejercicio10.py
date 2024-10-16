#se define la funcion PersInfor con los argumentos de Nom, AñoIn y Apell
def PersInfor (Nom, AñoIn, Apell):
    #se inicia la variable antiguedad como entero y en 0
    antiguedad = int(0)
    #se determina la antiguedad del empleado restandole al año actual (2024), el año de entrada a la empresa
    antiguedad = (2024 - AñoIn)
    #se retorna un mensaje en el que se incluyen los argumentos de Nom, Apell y la variable antiguedad
    return (f"Hola {Nom} {Apell}, felicitaciones, ya llevas {antiguedad} años con la compañía")
#Protecciòn principal (cuerpo programa)
if(__name__ == '__main__'):
    #se le pide al usuario que ingrese el valor o contenido de las variables Nombre, Apellidos, Telefono, Año y Edad
    Nombre = str(input('Ingrese su nombre: '))
    Apellidos = str(input('Ingrese sus apellidos: '))
    Telefono = int(input('Ingrese su telefono: '))
    Año = int(input('Ingrese el año de ingreso a la empresa: '))
    Edad = int(input('Ingrese su edad: '))
    #se imprime el retorno de la funcion PersInfor con los argumentos de Nombre, Año y Apellidos
    print(PersInfor(Nombre, Año, Apellidos))