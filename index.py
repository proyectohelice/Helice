
#probando desde el terminal.

import requests
from bs4 import BeautifulSoup
import lxml
from datetime import datetime, date, time, timedelta
import calendar

#############################################################
########### OBTENCION DE INFORMACION ########################


#  SALUDO DE BIENVENIDA Y SELECCION DE MENU
print("\n")
if datetime.now().hour <12 and datetime.now().hour>6:

	print("Muy buenos días por favor selecciona una opcion del siguiente menú:\n")

elif datetime.now().hour <20 and datetime.now().hour>=12:

	print("Muy buenas tardes por favor selecciona una opcion del siguiente menú:\n")

elif datetime.now().hour <=6 and datetime.now().hour>=20:

	print("Muy buenas noches por favor selecciona una opcion del siguiente menú:\n")

#  Presentacion de menú al usuario
print("1 - Xbox One\n2 - Play Station 4\n3 - Xbox 360\n4 - Wii\n5 - Nintendo Switch\n6 - Nintendo 3DS\n7 - Play Station Vita\n8 - Computador\n9 - Ofertas\n")

consola = input("Por favor ingrese un valor entre 1 - 9 para seleccionar:")


# Proceso de opcion de menu

if consola == '1': # si consola = 1 se elije consola xbox one
	url= "http://www.weplay.cl/resultado/juegos+xbox+one/1/creacion_mayor/"  #Url de juegos Xbox one.

elif consola == '2':

	url="http://www.weplay.cl/resultado/juegos+ps4/1/creacion_mayor/" #Url de juegos play station 4.

elif consola == '3':

	url="http://www.weplay.cl/resultado/juegos+xbox+360/1/creacion_mayor/" #Url de juegos xbox 360.

elif consola == '4':

	url="http://www.weplay.cl/resultado/juegos+wii/1/creacion_mayor/" #Url de juegos wii.

elif consola == '5':

	url="http://www.weplay.cl/resultado/juegos+switch/1/creacion_mayor/" #Url de juegos switch.

elif consola == '6':

	url="http://www.weplay.cl/resultado/juegos+3ds/1/creacion_mayor/" #Url de juegos 3ds.

elif consola == '7':

	url="http://www.weplay.cl/resultado/juegos+ps+vita/1/creacion_mayor/" #Url de juegos pc.

elif consola == '8':

	url="http://www.weplay.cl/resultado/juegos+pc/1/creacion_mayor/" #Url de juegos pc.

elif consola == '9':

	url="http://www.weplay.cl/liquidacion/todo/1/precio_menor" #Url de ofertas.
else:
	print("\n\n\n############################\nERROR!!!: Los numeros van entre 1-9\n############################\n\n\n")



 
# Capturamos el hml de la pagina web y creamos un objeto Response
r  = requests.get(url)
data = r.text

 
# Creamos el objeto soup y le pasamos lo capturado con request
soup = BeautifulSoup(data, 'lxml')

#Buscar en la pag todos las clases prod.
articulos = soup.find_all('div', class_="prod")
nombre = soup.find_all('div', class_="nom_prod")
precio = soup.find_all('div', class_="prec_prod_b")

#############################################################

#############################################################
########## PROCESAMIENTO DE LA INFORMACION #################


for i in range(0,6*4):
	print("--------------------------------------")
	print('numero producto:',i+1)
	print('-','nombre:', nombre[i].text)
	print('-','precio:',precio[i].text)










