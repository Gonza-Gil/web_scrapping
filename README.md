# Web Scraping
Este repositorio contiene varias apps desarrolladas en Python con el fin de aprender web scraping

## Requisitos
__Antes de ejecutar correr en consola:__<br>
```
pip install -r requirements.txt
```

## Map it
Es un programa que permite buscar una dirección en Google Maps. La dirección debe ser ingresada por teclado o puede usarse directamente una dirección presente en el portapapeles.<br>
El programa hace uso de la librería webbrowser para abrir el navegador en la página deseada, y de la librería pyperclip para poder copiar un texto desde el portapapeles.<br>
__Para ejecutarla correr en consola:__<br>
```
python mapit.py
```

## SearchPypi
Es un programa que permite realizar una búsqueda en [pypi](https://pypi.org/). Se debe ingresar en la consola lo que se quiera buscar en la página, y el programa abrirá
en el navegador una pestaña con los resultados de la búsqueda y otras pestañas con los primeros resultados.<br>
El programa hace uso de la librería webbrowser para abrir el navegador en la página deseada, de la librería requests para descargar el HTML de la página, y de la librería
bs4 para extraer del HTML los links de los resultados de la búsqueda.<br>
__Para ejecutarlo correr en consola:__<br>
```
python searchpypi.py
```

## SearchMELI
Es lo mismo que SearchPypi, con la diferencia de que permite hacer busquedas en Mercado Libre.<br>
__Para ejecutarlo correr en consola:__<br>
```
python search_meli.py
```

## Auto 2048
Es un programa que juega al juego [2048](https://gabrielecirulli.github.io/2048/). El programa lo que hace es mover las fichas con el patrón ARRIBA, DERECHA, ABAJO, IZQUIERDA, ya que de esta forma se pueden obtener puntajes bastante altos.<br>
__Para ejecutarlo correr en consola:__<br>
```
python auto_2048.py
```

## Recursos
- [Web scraping](https://es.wikipedia.org/wiki/Web_scraping)
- [Webbrowser](https://docs.python.org/es/3/library/webbrowser.html)
- [Requests](https://docs.python-requests.org/en/latest/)
- [BS4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Pyperclip](https://pypi.org/project/pyperclip/)
- [Selenium](https://www.selenium.dev/documentation/)
