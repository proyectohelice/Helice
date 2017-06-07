

import requests
from bs4 import BeautifulSoup

url = 'http://www.apolinav.cl'# Direccion de la pagina web.

#Peticion a la pagina web.

req = requests.get(url)

# comprobacion de peticion aceptada

status_code = req.status_code

if status_code == 200:
	
	#pasamos el contenido HTML de la web a un objeto Bs4()
	html = BeautifulSoup(req.text,"html.parser")

	#Obtecion de todos los divs donde estan las entradas
	entradas = html.find_all('div',{'class': 'col-md-4 col-cs-12'})

	#recorremos las entradas para extraer el titulo, autor y fecha
	for i, entrada in enumerate(entradas):
		#con el metodo "getText()" no nos devuelve el HTML
		titulo= entrada.find('span',{'class':'tituloPost'}).getText()
		#sino llamaos al metodo "getText()" nos devuelve tambien el HTML
		autor = entrada.find('span',{'class':'autor'})
		fecha = entrada.find('span',{'class':'fecha'}).getText()

		#imprimir titulo, autor y fecha de entradas
		print "%d - %s | %s | %s" % (i+1,titulo,autor,fecha)
else:
	print "Status Code %d" % status_code

# comentario de prueba




