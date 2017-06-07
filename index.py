
#probando desde el terminal.

import requests
from bs4 import BeautifulSoup



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

<<<<<<< HEAD
print(nombre[1].text)
print(precio[1].text)
=======
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
>>>>>>> 25d96e54fdca207bdaa12d141c4a31d05a5e809f




