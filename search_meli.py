# App WebScrapper para la página Mercado Libre
# La misma permite ingresar lo que se quiere buscar y esta abre automaticamente una pestaña del navegador
# mostrando los resultados de la busqueda y a su vez abre en otras pestañas los primeros resultados

import requests, bs4, webbrowser

busqueda = input("Qué desea buscar en Mercado Libre? ")
webbrowser.open('https://listado.mercadolibre.com.ar/' + busqueda + '#D[A:' + busqueda + ']')
res = requests.get('https://listado.mercadolibre.com.ar/' + busqueda + '#D[A:' + busqueda + ']')
busqueda_soup = bs4.BeautifulSoup(res.text, 'html.parser')
links = busqueda_soup.select('a.ui-search-item__group__element')
for i in range(min(5, len(links))):
    l = links[i].get('href')
    webbrowser.open(l)