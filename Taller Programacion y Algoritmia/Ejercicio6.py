#se define la funcion Fecha
def fecha (Dia, Mes, Año):
    #se inician en false las variables booleanas DiasVerificacion, MesVerificacion y AñoVerificacion
    DiaVerificacion = False
    MesVerificaion = False
    AñoVerificacion = False
    #condicionales para determinar si el día, mes y año ingresado por el usuario es valido como fecha
    if (0<Dia<=31):
        DiaVerificacion=True
    if (0<Mes<=12):
        MesVerificaion=True
    if (0<Año<=2024):
        AñoVerificacion=True
    #condicional que determina si el año ingresado es bisiesto o no
    if (((Año % 4) == 0) and ((Año % 100) != 0) or ((Año % 400)==0)):
        TipoAño='es bisiesto'
    else : 
        TipoAño='no es bisiesto'
    #condicional que, si las variables DiaVerificacion, MesVerificaion y AñoVerificacion son correctas, imprime en pantalla que la fecha indicada es correcta y el tipo de año
    if (DiaVerificacion == True and MesVerificaion == True and AñoVerificacion== True):
        print(f"La fecha indicada es valida y el año indicado {TipoAño}")
    else:
        print('La fecha indicada no es valida')
#Protecciòn principal (cuerpo programa)
if(__name__=='__main__'):
    #Se inician en 0 y como entero las variables día, mes y año
    Dia= int(0)
    Mes= int(0)
    Año= int(0)
    #Se le pide al usuario ingresar las variables Dia, mes y año
    Dia = int(input('ingrese el dìa del año: '))
    Mes = int(input('ingrese el Mes del año: '))
    Año = int(input('ingrese el Año: '))
    #Se llama o invoca la funcion fecha
    fecha(Dia, Mes, Año)