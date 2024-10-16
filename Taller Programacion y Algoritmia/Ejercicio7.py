#se define la funcion triangulo con los argumentos L1,L2 y L3
def triangulo (L1,L2,L3):
    #se inicia en false la variable booleana DesTriangulo
    DesTriangular = bool(False)
    #se evalua la desigualdad triangular de los lados dados por el usuario
    if (L1+L2>L3):
        DesTriangular = True
    elif (L1+L3>L2):
        DesTriangular = True
    elif (L2+L3>L1):
        DesTriangular = True
    #mensaje en caso tal de que la desigualdad triangular no se cumpla
    else:
        print('Los lados ingresados no corresponden a un triangulo valido según la Desigualdad Triangular')
    #si la desigualdad triangular se cumple, se muestra un mensaje en patalla que lo indica
    if (DesTriangular):
        print('Las longitudes de los lados ingresados sí corresponden a las de un triangulo valido según la Desigualdad Triangular')
#Protecciòn principal (cuerpo programa)
if(__name__ == '__main__'):
    #se le pide al usuario que ingrese 
    L1 = int(input('Ingrese el valor del primer lado del triangulo: '))
    L2 = int(input('Ingrese el valor del segundo lado del triangulo: '))
    L3 = int(input('Ingrese el valor del tercer lado del triangulo: '))
    #se llama y/o invoca la funcion triangulo con los argumentos L1,L2 y L3
    triangulo(L1,L2,L3)