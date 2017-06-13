import socket# se importa la funcion socket para comprobar conexion

def Prueba_Conexion(url):#funcion que contiene las try o except para mostrar el resultado de la conexion
    prueba = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#crea un socket INET del tipo STREAM
    try:
        prueba.connect((url, 80))#se conecta al servidor web por el puerto 80
        print ("Pagina on-line. Iniciando programa.")
        prueba.close()
    except:
        print ("Lo sentimos, pero no se ha podido establecer la conexión.")
        quit()#en el caso que no exista conexion, la funcion interrumpe el programa
    prueba.close()



