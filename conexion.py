import socket

def IsInternetUp():
    testConn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        testConn.connect(('http://www.apolinav.cl', 80))
        print ("Estamos on-line. Ya podemos iniciar el programa.")
        testConn.close()
    except:
        print ("Lo sentimos, pero no se ha podido establecer la conexión.")
        quit()
    testConn.close()

IsInternetUp()
