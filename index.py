
#probando desde el terminal.

import requests
from bs4 import BeautifulSoup
import lxml


#############################################################
########### OBTENCION DE INFORMACION ########################



# Capturamos la url ingresada en la variable "url"
url = 'http://www.weplay.cl'
 
# Capturamos el hml de la pagina web y creamos un objeto Response
r  = requests.get(url)
data = r.text

 
# Creamos el objeto soup y le pasamos lo capturado con request
soup = BeautifulSoup(data, 'lxml')

#Buscar en la pag todos las clases prod.
articulos = soup.find_all('div', class_="prod")
nombre = soup.find_all('div', class_="nom_prod")
precio = soup.find_all('div', class_="prec_prod")

#############################################################

#############################################################
########## PROCESAMIENTO DE LA INFORMACION #################


for i in range(0,6):
	print("--------------------------------------")
	print('numero:',i)
	print('-','nombre:', nombre[i].text)
	print('-','precio:',precio[i].text)










