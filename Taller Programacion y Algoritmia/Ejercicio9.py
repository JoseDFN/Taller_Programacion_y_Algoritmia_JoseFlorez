#se define la funcion promedio con el argumento cantidad
def Promedio (Cantidad):
    #se inicia la variable contador, sumatoria y promedio como entero y en 0
    i=int(0)
    Sumatoria = int(0)
    Promedio = int(0)
    #bucle que se ejecuta mientras la variable contador sea menor a la variable cantidad (ingresada por el usuario)
    while (i<Cantidad):
        #se le suma uno a la variable contador
        i+=1
        #se le pide un numero al usuario
        NumeroUsuario = int(input(f"Ingrese el numero {i}: "))
        #se rompe el bucle si se ingresa un numero negativo
        if (NumeroUsuario < 0):
            break
        #sumatoria de los valores ingreados por el usuario
        Sumatoria += NumeroUsuario
    #se saca el promedio con la variable sumatoria y el valor del contador
    Promedio = (Sumatoria/i)
    #retorna la variable promedio
    return Promedio
#Protecciòn principal (cuerpo programa)
if(__name__ == '__main__'):
    #el usuario ingresa la cantidad de numeros a sumar
    CantNumU=int(input('Ingrese la cantidad de numeros que quiere ingresar: '))
    #se imprime la variable que retorna la funcion Promedio
    print (Promedio(CantNumU))