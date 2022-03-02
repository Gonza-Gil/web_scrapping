# Codigo que juega automaticamente al juego 2048
# Se puede obtener un putaje bastante alto haciendo la secuencia ARRIBA, DERECHA, ABAJO, IZQUIERDA
# Eso es exactamente lo que hace el codigo, hasta detectar que perdió la partida

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://gabrielecirulli.github.io/2048/")

time.sleep(5)
htmlElem = driver.find_element_by_tag_name('html')
while True:
    try:
        search_play_again = driver.find_element_by_link_text("Try again")
        break
    except:        
        print("ARRIBA")
        htmlElem.send_keys(Keys.ARROW_UP)
        time.sleep(0.5)
        print("DERECHA")
        htmlElem.send_keys(Keys.ARROW_RIGHT)
        time.sleep(0.5)
        print("ABAJO")
        htmlElem.send_keys(Keys.ARROW_DOWN)
        time.sleep(0.5)
        print("IZQUIERDA")
        htmlElem.send_keys(Keys.ARROW_LEFT)
        time.sleep(0.5)
        
print("GAME OVER")
time.sleep(10)

driver.quit()