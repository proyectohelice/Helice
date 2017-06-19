

def menu(consola):
    if consola == '1': # si consola = 1 se elije consola xbox one
        url= "http://www.weplay.cl/resultado/juegos+xbox+one/1/creacion_mayor/"  #Url de juegos Xbox on
        name='xbox one'
        comprobacion='1'
    elif consola == '2':
        url="http://www.weplay.cl/resultado/juegos+ps4/1/creacion_mayor/" #Url de juegos play station 4.
        name="play station 4"
        comprobacion='1'
    elif consola == '3':
        url="http://www.weplay.cl/resultado/juegos+xbox+360/1/creacion_mayor/" #Url de juegos xbox 360.
        name="xbox 360"
        comprobacion='1'
    elif consola == '4':
        url="http://www.weplay.cl/resultado/juegos+wii/1/creacion_mayor/" #Url de juegos wii.
        name="Wii"
        comprobacion='1'
    elif consola == '5':
        url="http://www.weplay.cl/resultado/juegos+switch/1/creacion_mayor/" #Url de juegos switch.
        name="Nintendo Switch"
        comprobacion='1'
    elif consola == '6':
        url="http://www.weplay.cl/resultado/juegos+3ds/1/creacion_mayor/" #Url de juegos 3ds.
        name="Nintendo 3ds"
        comprobacion='1'
    elif consola == '7':
        url="http://www.weplay.cl/resultado/juegos+ps+vita/1/creacion_mayor/" #Url de juegos vita.
        name="PS vita"
        comprobacion='1'
    elif consola == '8':
        url="http://www.weplay.cl/resultado/juegos+pc/1/creacion_mayor/" #Url de juegos pc.
        name="PC"
        comprobacion='1'
    elif consola == '9':
        url="http://www.weplay.cl/liquidacion/todo/1/precio_menor" #Url de ofertas.
        name="Ofertas"
        comprobacion='1'
    else:
        comprobacion='0'
        url="no existe"
        name="no existe"

    return url,name,comprobacion
    
