# App WebScrapper para la página pypi.org
# La misma permite ingresar lo que se quiere buscar y esta abre automaticamente una pestaña del navegador
# mostrando los resultados de la busqueda y a su vez abre en otras pestañas los primeros resultados

import requests, bs4, webbrowser

busqueda = input("Qué desea buscar en pypi.org? ")
webbrowser.open('https://pypi.org/search/?q=' + busqueda)
res = requests.get('https://pypi.org/search/?q=' + busqueda)
busqueda_soup = bs4.BeautifulSoup(res.text, 'html.parser')
links = busqueda_soup.select('.package-snippet')
for i in range(min(5, len(links))):
    l = links[i].get('href')
    webbrowser.open('https://pypi.org' + l)