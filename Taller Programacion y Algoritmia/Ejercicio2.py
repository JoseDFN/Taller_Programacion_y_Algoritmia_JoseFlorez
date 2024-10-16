#Se define la funcion Numero final to Numero inicio (NfTNi)
def NumerofinalaNumeroinicial(Numero):
    #se define la variable contador
    i = int(1)
    #bucle while en el que se irà imprimiendo el numero ingresado por el usuario y se le resta 1, hasta que este sea igual a 1
    while(Numero>=1):
        print(Numero)
        Numero-=1
#Protecciòn principal    
if (__name__=='__main__'):
    #se le pide un numero al usuario que ingrese un numero
    Numero = int(input('Ingrese un entero positivo: '))
    #imprimir el resultado que da la funcion main al invocarlo.
    NumerofinalaNumeroinicial(Numero)