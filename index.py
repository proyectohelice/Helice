
#importacion de bibliotecas.

import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, time, timedelta
import lxml
import calendar
import xlwt
import Juegos

#importacion de Funciones

import conexion #llama a la funcion conexion.py para determinar si hay conexion a internet

import saludo #llama a la funcion saludo.py para determinar la hora del dia y saludar correctamente

import menus #Llama a la funcion que acciona el menu

#  Presentacion de menú al usuario
print("1 - Xbox One\n2 - Play Station 4\n3 - Xbox 360\n4 - Wii\n5"+ 
	"- Nintendo Switch\n6 - Nintendo 3DS\n7 - Play Station Vita\n8 "+
	"- Computador\n9 - Ofertas\n")

consola = input("Por favor ingrese un valor entre 1 - 9 para seleccionar:")


# Proceso de opcion de menu

[url,name,comprobacion]=menus.menu(consola) #Funcion de menu


if comprobacion == '1':
        pagina='www.weplay.cl'
        conexion.Prueba_Conexion(pagina)   #Efectua prueba de Conexion a la pagina Web.

	# Capturamos el hmtl de la pagina web
        r  = requests.get(url)
        data = r.text

 
	# Creamos el objeto soup y le pasamos lo capturado con request
        soup = BeautifulSoup(data, 'lxml')

	#Buscar en la pag todos las clases que contienen nombre y precio.
        articulos = soup.find_all('div', class_="prod") # del codigo HTML de la pagina web se toda la clase "prod", 
        nombre = soup.find_all('div', class_="nom_prod")# del codigo HTML de la pagina web se toma la clase "nom_prod", 
        precio = soup.find_all('div', class_="prec_prod_b")# del codigo HTML de la pagina web se toma la clase "prec_prod_b",
        for i in range(0,6*4):
                nombre[i]=nombre[i].text     #Saca cabecera sobrante
                nombre[i]=nombre[i].strip()  #Elimina los espacios extra
                precio[i]=precio[i].text
                precio[i]=precio[i].strip()
        juego=['','','','','','','','','','','','','','','','','','','','','','','','']

        #Creacion Objetos
        for i in range(0,24):
                juego[i]=Juegos.juegos(name,precio[i],nombre[i])


        print("--------------------------------------------------------------------------------------------------------------")
        print("       CONSOLA     |                           PRECIO y NOMBRE      ")
        print("--------------------------------------------------------------------------------------------------------------")
        for i in range(0,24):
                juego[i].Consola();juego[i].Nombre();juego[i].Precio()

        print("\n\n¿Le gustaria Guardar los datos en un archivo Excel?\n")
        si_o_no=input("Por favor ingrese '1' para SI y '2' para NO:")

        import despedida#ejecuta la funcion para indicar el guardado de lo solicitado y termino con despedida
        
        if si_o_no == "1":

         despedida.termino('excel')
         estilo= xlwt.easyxf('font: name Times New Roman, colour black, bold on')
         wb = xlwt.Workbook()
         pestana = wb.add_sheet(name,cell_overwrite_ok=True) #Crea pestana con nombre de categoria
         pestana.write(0, 0, 'NOMBRE', estilo)
         pestana.write(0, 1, 'PRECIO', estilo)

        
         for i in range(0,6*4):   #Se escriben las celdas excel.
                pestana.write(i+1, 0, nombre[i], estilo)
                pestana.write(i+1, 1, precio[i], estilo)

         wb.save('Weplay.xls') #Se guarda archivo Excel. 
         despedida.termino('adios1')
        elif si_o_no == "2":
         despedida.termino('adios2')
        else:
                print("\n\n\n############################\n"+"\x1b[0;37;41m"+"ERROR: Numero ingresado no encontrado"+"\x1b[0m"+" \n############################\n\n\n")

elif comprobacion == '0':
        print("\n\n\n############################\n"+"\x1b[0;37;41m"+"ERROR: Numero ingresado no encontrado"+"\x1b[0m"+" \n############################\n\n\n")



