def salute(hora):#funcion en la cual toma el valor de la variable hola
    if hora<12 and hora>0:#condicion en la cual verifica el valor y saluda de acuerdo al horario del dia
        print('Muy buenos dias, por favor seleccione un producto a consultar del siguiente menu:')
    elif hora>=12 and hora<20:
        print('Muy buenas tardes, por favor seleccione un producto a consultar del siguiente menu:')
    elif hora>=20:
        print('Muy buenas noches, por favor seleccione un producto a consultar del siguiente menu:')
from datetime import datetime, date, time, timedelta#importa datetime que contiene el valor de la hora actual
salute(datetime.now().hour)#le asigna el valor de datetime a la variable hora para entrar a la funcion e iniciarla
