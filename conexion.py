import socket# se importa la funcion socket para comprobar conexion

def IsInternetUp():#funcion que contiene las try o except para mostrar el resultado de la conexion
    testConn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#crea un socket INET del tipo STREAM
    try:
        testConn.connect(('http://www.apolinav.cl', 80))#se conecta al servidor web por el puerto 80
        print ("Estamos on-line. Ya podemos iniciar el programa.")
        testConn.close()
    except:
        print ("Lo sentimos, pero no se ha podido establecer la conexión.")
        quit()#en el caso que no exista conexion, la funcion interrumpe el programa
    testConn.close()

IsInternetUp()#ejecuta la funcion
