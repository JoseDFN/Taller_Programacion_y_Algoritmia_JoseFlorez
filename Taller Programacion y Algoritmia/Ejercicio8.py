#Se define la funcion TablaMult con argumento Num
def TablaMult (Num):
    #se incian las variables NmultI y ResultadoMult en 0 y como enteros
    NMultI = int(0)
    ResultadoMult=int(0)
    #bucle while para imprimir las tablas de multiplicar con su respectivo resultado
    while(NMultI<Num):
        NMultI+=1
        print(NMultI, (NMultI*Num))
#Protecciòn principal (cuerpo programa)
if(__name__ == '__main__'):
    #se le pide al usuario ingresar el numero
    NumeroUsuario = int(input('Ingrese un numero para ver su tabla de multiplicar del 1 al 10: '))
    #se invoca la funcion teniendo como argumento a NumeroUsuario
    TablaMult(NumeroUsuario)