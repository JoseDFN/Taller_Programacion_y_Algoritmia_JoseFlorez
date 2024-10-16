#Se define la variable CalificacionAprobadoOReprobado
def CalificacionAprobadoOReprobado (Nota):
    #si la nota es mayor o igual a 60, el estudiante aprueba, sino, el estudiante queda reprobado
    if Nota>=60:
        return('Has aprobado')
    else:
        return('Reprobado')
#Protecciòn principal    
if (__name__=='__main__'):
    #se le pide al usuario que ingrese la nota (de 0 a 100)
    Nota = int(input('Ingrese su nota(0-100): '))
    #imprimir el resultado o retorno de la funcion al invocarla
    print(CalificacionAprobadoOReprobado(Nota))