#se define la variable determinar continente
def detContinente (Pais):
    #se definen las variables continentes con sus respectivos países en ellas
    NorteAmerica = ['USA', 'CANADA']
    CentroAmerica = ['MEXICO', 'PANAMA', 'HONDURAS', 'GUATEMALA']
    SurAmerica = ['COLOMBIA', 'ECUADOR', 'PERU', 'BRAZIL', 'ARGENTINA', 'CHILE']
    Europa = ['ESPAÑA', 'FRANCIA', 'ALEMANIA', 'BELGICA', 'POLONIA']
    Asia = ['CHINA', 'JAPON', 'KOREA', 'FILIPINAS', 'TAIWAN']
    Africa = ['NIGERIA', 'MARRUECOS', 'TANZANIA', 'UGANDA']
    #se evalua si el país ingresado se encuentra en alguna de las variables continentes definidas
    if Pais in NorteAmerica:
        return ('Su pais esta en Norte america')
    elif Pais in CentroAmerica:
        return ('Su pais esta en Centro america')
    elif Pais in SurAmerica:
        return ('Su pais esta en Sur america')
    elif Pais in Europa:
        return ('Su pais esta en Europa')
    elif Pais in Asia:
        return ('Su pais esta en Asia')
    elif Pais in Africa:
        return ('Su pais esta en Africa')
    #mensaje en caso tal de que el país ingresado no se encuentre dentro de los paises en las variables continentes
    else:
        return ('Lo sentimos, el país ingresado no se encuentra en nuestra lista de paises en estos momentos.')
#Protecciòn principal (cuerpo programa)
if (__name__=='__main__'):
    #se le pide al usuario ingresar el país
    pais = str(input('Ingrese el país: ')).upper()
    #se imprime el resultado  de la busqueda del país de la funcion detContinente
    print(detContinente(pais))