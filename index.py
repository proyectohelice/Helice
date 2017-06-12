
#probando desde el terminal.

import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, time, timedelta
import lxml
import calendar
import xlwt

#############################################################
########### OBTENCION DE INFORMACION ########################
#Comprobar la conexion de internet

import conexion

#  SALUDO DE BIENVENIDA Y SELECCION DE MENU

import saludo

#  Presentacion de menú al usuario
print("1 - Xbox One\n2 - Play Station 4\n3 - Xbox 360\n4 - Wii\n5 - Nintendo Switch\n6 - Nintendo 3DS\n7 - Play Station Vita\n8 - Computador\n9 - Ofertas\n")

consola = input("Por favor ingrese un valor entre 1 - 9 para seleccionar:")


# Proceso de opcion de menu

if consola == '1': # si consola = 1 se elije consola xbox one
	url= "http://www.weplay.cl/resultado/juegos+xbox+one/1/creacion_mayor/"  #Url de juegos Xbox one.
	name='xbox one'

elif consola == '2':

	url="http://www.weplay.cl/resultado/juegos+ps4/1/creacion_mayor/" #Url de juegos play station 4.
	name="play station 4"

elif consola == '3':

	url="http://www.weplay.cl/resultado/juegos+xbox+360/1/creacion_mayor/" #Url de juegos xbox 360.
	name="xbox 360"

elif consola == '4':

	url="http://www.weplay.cl/resultado/juegos+wii/1/creacion_mayor/" #Url de juegos wii.
	name="Wii"

elif consola == '5':

	url="http://www.weplay.cl/resultado/juegos+switch/1/creacion_mayor/" #Url de juegos switch.
	name="Nintendo Switch"

elif consola == '6':

	url="http://www.weplay.cl/resultado/juegos+3ds/1/creacion_mayor/" #Url de juegos 3ds.
	name="Nintendo 3ds"

elif consola == '7':

	url="http://www.weplay.cl/resultado/juegos+ps+vita/1/creacion_mayor/" #Url de juegos vita.
	name="PS vita"

elif consola == '8':

	url="http://www.weplay.cl/resultado/juegos+pc/1/creacion_mayor/" #Url de juegos pc.
	name="PC"

elif consola == '9':

	url="http://www.weplay.cl/liquidacion/todo/1/precio_menor" #Url de ofertas.
	name="Ofertas"
else:
	print("\n\n\n############################\n"+"\x1b[0;37;41m"+"ERROR: Numero ingresado no encontrado"+"\x1b[0m"+" Numero ingresado no encontrado\n############################\n\n\n") 



 
# Capturamos el hml de la pagina web
r  = requests.get(url)
data = r.text

 
# Creamos el objeto soup y le pasamos lo capturado con request
soup = BeautifulSoup(data, 'lxml')

#Buscar en la pag todos las clases que contienen nombre y precio.

articulos = soup.find_all('div', class_="prod")

nombre = soup.find_all('div', class_="nom_prod")
precio = soup.find_all('div', class_="prec_prod_b")

#############################################################

#############################################################
########## PROCESAMIENTO DE LA INFORMACION #################


#for i in range(0,6*4):
#	print("--------------------------------------")
#	print('numero producto:',i+1)
#	print('-','nombre:', nombre[i].text)
#	print('-','precio:',precio[i].text)

# Creacion archivo Excel con Solo el primer resultado.

estilo= xlwt.easyxf('font: name Times New Roman, colour black, bold on')
wb = xlwt.Workbook()
pestana = wb.add_sheet(name,cell_overwrite_ok=True) #Crea pestana
pestana.write(0, 0, '                       NOMBRE', estilo)
pestana.write(0, 1, '                       PRECIO', estilo)

for i in range(0,6*4):
        pestana.write(i+1, 0, nombre[i].text, estilo)
        pestana.write(i+1, 1, precio[i].text, estilo)
wb.save('Weplay.xls')








