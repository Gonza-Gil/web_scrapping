# Web Scraping
Este repositorio contiene varias apps desarrolladas en Python con el fin de aprender web scraping

## Requisitos
__Antes de ejecutar correr en consola:__<br>
```
pip install -r requirements.txt
```

## Map it
Es un programa que permite buscar una dirección en google maps. La dirección debe ser ingresada por teclado o puede usarse directamente una dirección presente en el portapapeles.<br>
El programa hace uso de la libreria webbrowser para abrir el navegador en la página deseada, y de la libreria pyperclip para poder copiar un texto desde el portapapeles.<br>
__Para ejecutarla correr en consola:__<br>
```
python mapit.py
```

## SearchPypi
Es un programa que permite buscar realizar una busqueda en [pypi](https://pypi.org/). Se debe ingresar en la consola lo que se quiera buscar en la página, y el programa abrirá
en el navegador una pestaña con los resultados de la busqueda y otras pestañas con los primeros resultados.<br>
El programa hace uso de la libreria webbrowser para abrir el navegador en la página deseada, de la libreria requests para descargar el HTML de la página, y de la librería
bs4 para extraer del HTML los links de los resultados de la busqueda.<br>
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
