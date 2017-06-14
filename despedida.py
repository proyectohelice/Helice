def termino(ending):
    if ending=='excel':#condicion para indicar que esta generando el ecxel
        print('Generando archivo Weplay.xls con informacion solicitada.')
    elif ending=='adios':
        print('archivo guardado en el escritorio con exito.')#condicion para indicar que el archivo se guardo ya que se ejecuto archivo.save()
        from datetime import datetime, date, time, timedelta
        hora=datetime.now().hour
        if hora<12 and hora>0:#condicion en la cual verifica el valor para despedirse
            print('Gracias por usar Collector, Que tenga un buen dia.')
        elif hora>=12 and hora<20:
            print('Gracias por usar Collector, Que tenga una buena tarde')
        elif hora>=20:
            print('Gracias por usar Collector, Buenas noches.')
