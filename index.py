
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
        lista=dict()   #Crea diccionario con lista de juegos
        for i in range(0,6*4):
                lista[nombre[i]]=precio[i]

        #Creacion de los objetos.
        juego0=Juegos.juegos(name,precio[0],nombre[0])
        juego1=Juegos.juegos(name,precio[1],nombre[1])
        juego2=Juegos.juegos(name,precio[2],nombre[2])
        juego3=Juegos.juegos(name,precio[3],nombre[3])
        juego4=Juegos.juegos(name,precio[4],nombre[4])
        juego5=Juegos.juegos(name,precio[5],nombre[5])
        juego6=Juegos.juegos(name,precio[6],nombre[6])
        juego7=Juegos.juegos(name,precio[7],nombre[7])
        juego8=Juegos.juegos(name,precio[8],nombre[8])
        juego9=Juegos.juegos(name,precio[9],nombre[9])
        juego10=Juegos.juegos(name,precio[10],nombre[10])
        juego11=Juegos.juegos(name,precio[11],nombre[11])
        juego12=Juegos.juegos(name,precio[12],nombre[12])
        juego13=Juegos.juegos(name,precio[13],nombre[13])
        juego14=Juegos.juegos(name,precio[14],nombre[14])
        juego15=Juegos.juegos(name,precio[15],nombre[15])
        juego16=Juegos.juegos(name,precio[16],nombre[16])
        juego17=Juegos.juegos(name,precio[17],nombre[17])
        juego18=Juegos.juegos(name,precio[18],nombre[18])
        juego19=Juegos.juegos(name,precio[19],nombre[19])
        juego20=Juegos.juegos(name,precio[20],nombre[20])
        juego21=Juegos.juegos(name,precio[21],nombre[21])
        juego22=Juegos.juegos(name,precio[22],nombre[22])
        juego23=Juegos.juegos(name,precio[23],nombre[23])

        print("--------------------------------------------------------------------------------------------------------------")
        print("       CONSOLA     |                           PRECIO y NOMBRE      ")
        print("--------------------------------------------------------------------------------------------------------------")
        juego0.Consola();juego0.Nombre();juego0.Precio()
        juego1.Consola();juego1.Nombre();juego1.Precio()
        juego2.Consola();juego2.Nombre();juego2.Precio()
        juego3.Consola();juego3.Nombre();juego3.Precio()
        juego4.Consola();juego4.Nombre();juego4.Precio()
        juego5.Consola();juego5.Nombre();juego5.Precio()
        juego6.Consola();juego6.Nombre();juego6.Precio()
        juego7.Consola();juego7.Nombre();juego7.Precio()
        juego8.Consola();juego8.Nombre();juego8.Precio()
        juego9.Consola();juego9.Nombre();juego9.Precio()
        juego10.Consola();juego10.Nombre();juego10.Precio()
        juego11.Consola();juego11.Nombre();juego11.Precio()
        juego12.Consola();juego12.Nombre();juego12.Precio()
        juego13.Consola();juego13.Nombre();juego13.Precio()        
        juego14.Consola();juego14.Nombre();juego14.Precio()
        juego15.Consola();juego15.Nombre();juego15.Precio()
        juego16.Consola();juego16.Nombre();juego16.Precio()
        juego17.Consola();juego17.Nombre();juego17.Precio()
        juego18.Consola();juego18.Nombre();juego18.Precio()
        juego19.Consola();juego19.Nombre();juego19.Precio()
        juego20.Consola();juego20.Nombre();juego20.Precio()
        juego21.Consola();juego21.Nombre();juego21.Precio()
        juego22.Consola();juego22.Nombre();juego22.Precio()
        juego23.Consola();juego23.Nombre();juego23.Precio()


        import despedida#ejecuta la funcion para indicar el guardado de lo solicitado y termino con despedida
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
        despedida.termino('adios')

elif comprobacion == '0':
        print("\n\n\n############################\n"+"\x1b[0;37;41m"+"ERROR: Numero ingresado no encontrado"+"\x1b[0m"+" \n############################\n\n\n")



