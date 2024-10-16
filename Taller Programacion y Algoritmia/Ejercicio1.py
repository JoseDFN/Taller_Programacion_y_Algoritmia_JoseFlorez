#definicion funciòn edad
def MayoroMenor(Edad):
    #Se le pide al usuario que ingrese su edad
    #condicional que retorna 'Eres mayor de edad' y 'Eres menor de edad' si eres mayor o menor de 18
    if (Edad>=18):
        return ('Eres mayor de edad')
    else:
        return('Eres menor de edad')
#Protecciòn principal    
if (__name__=='__main__'):
    #imprimir el resultado que da la funcion main al invocarlo.
    Edad = int(input('Ingrese su edad: '))
    print(MayoroMenor(Edad))