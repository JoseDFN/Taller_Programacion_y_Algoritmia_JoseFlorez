#se define la funcion ValorEnergiaTotal en la que se calcula el valor final a pagar con base en el precio por kw, la cantidad de kw usados en el mes y el estrato
def ValorEnergiaTotal (KwPrecio, KwTotal, Estrato):
    #se define la variable ValorFinal en 0 y como una variable float
    ValorFinal = float(0)
    #variable TotalPagarADescuentos que es el resultado de la multiplicacion del precio po kw y la cantidad de los kw usados
    TotalPagarADescuentos = (KwPrecio*KwTotal)
    #funcion match para determinar el valor final a pagar con base en el estrato y la variable TotalPagarADescuentos
    match Estrato:
        case 1:
            ValorFinal = TotalPagarADescuentos*0.3
        case 2:
            ValorFinal = TotalPagarADescuentos*0.6
        case 3: 
            ValorFinal = TotalPagarADescuentos*0.85
        case 4:
            ValorFinal = TotalPagarADescuentos
        case 5:
            ValorFinal = TotalPagarADescuentos*1.15
        case 6:
            ValorFinal = TotalPagarADescuentos*1.25
        case _:
            print('El estrato ingresado no es  valido')
    #retorna la variable ValorFinal como respuesta
    return ValorFinal
#Protecciòn principal (cuerpo del programa)
if(__name__=="__main__"):
    #se le pide al usuario ingresar el mes del consumo, el valor por kw, la cantidad de kw usados y el estrato
    Mes_Consumo = int(input('Ingrese el mes (0-12): '))
    ValorKw = float(input('Ingrese el valor del Kw: '))
    TotalKwConsumidoMes = int(input('Ingrese la cantidad total de Kw consumidos: '))
    Estrato = int(input('Ingrese el estrato de su vivienda (0-6): '))
    #se invoca la funcion ValorEnergia total y se da una respuesta con base en esta.
    print(f"El valor a pagar de energía en el mes {Mes_Consumo} es:{ValorEnergiaTotal (TotalKwConsumidoMes, ValorKw, Estrato):.2f}")
    