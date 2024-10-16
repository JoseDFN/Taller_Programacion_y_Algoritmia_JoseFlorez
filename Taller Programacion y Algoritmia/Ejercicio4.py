#se define la variable requisitos
def requisitos (ContraseñaUsuario):
    #se establece la variable para verificar si dentro de ContraseñaUsuario existe un numero
    VariableNum = ('0123456789')
    #se inicia un contador para llevar la cantidad de numeros en ContraseñaUsuario
    a=int(0)
    #bucle en el que se le asigna a i cada caracter de la variable ContraseñaUsuario
    for i in ContraseñaUsuario:
        #condicional que evalua si i se encuentra en VariableNum y suma 1 al contador a
        if i in VariableNum :
            a+=1
    #condicional que determina si a es mayor o igual a 1 (validar que hay al menos 1 numero) y si el tamaño de la contraseña es al menos 8 caracteres
    if ((a>=1) and (len(ContraseñaUsuario)>=8)):
        #retorna 'Contraseña valida' si las condiciones se cumplen
        return ('Contraseña vàlida')
    else:
        #retorna 'Contraseña invalida' si las condiciones no se cumplen
        return('Contraseña invàlida')
#Protecciòn principal    
if (__name__=='__main__'):
    #se le pide al usuario que ingrese la contraseña
    Contra = ((input('Ingrese la contraseña: ')))
    #se imprime el retorno de la funcion requisitos (si la contraseña tiene al menos 1 numero y si su longitud es de al menos 8 caracteres)
    print(requisitos(Contra))