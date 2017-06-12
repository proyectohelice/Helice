def salute(hora):
    if hora<12 and hora>0:
        print('Muy buenos dias, por favor seleccione un producto a consultar del siguiente menu:')
    elif hora>=12 and hora<20:
        print('Muy buenas tardes, por favor seleccione un producto a consultar del siguiente menu:')
    elif hora>=20:
        print('Muy buenas noches, por favor seleccione un producto a consultar del siguiente menu:')
from datetime import datetime, date, time, timedelta
salute(datetime.now().hour)
