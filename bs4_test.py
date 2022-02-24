# Test de la libreria Beatiful Soup 4

import requests, bs4

# El metodo get de requests devuelve un objeto de tipo request, que contiene todo el contenido de la página en un string
res = requests.get('https://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(noStarchSoup))

# Con el objeto de tipo BeatifulSoup ahora puedo obtener distintos elementos del HTML de una página
# soup.select('div')                        All elements named <div>
# soup.select('#author')                    The element with an id attribute of author
# soup.select('.notice')                    All elements that use a CSS class attribute
#                                           named notice
# soup.select('div span')                   All elements named <span> that are within
#                                           an element named <div>
# soup.select('div > span')                 All elements named <span> that are
#                                           directly within an element named <div>,
#                                           with no other element in between
# soup.select('input[name]')                All elements named <input> that have a
#                                           name attribute with any value
# soup.select('input[type="button"]')       All elements named <input> that have an
#                                           attribute named type with value button

elems = noStarchSoup.select('#skip-link')
print(elems)
