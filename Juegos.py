


class juegos:

    def __init__(self, consola, precio, nombre):
    
        self.precio= precio
        self.consola=consola
        self.nombre=nombre
    def Precio(self):
        
            print("  -  " + self.precio+"\n--------------------------------------------------------------------------------------------------------------")

    def Consola(self):
            print ("      "+self.consola,end="    |         ")
     
    def Nombre(self):
            print (self.nombre,end="     ")
