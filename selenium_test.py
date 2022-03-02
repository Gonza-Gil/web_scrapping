import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://www.google.com")

search_box = driver.find_element_by_name('q')

search_box.send_keys('Selenium python')

search_box.submit()

time.sleep(5) # Let the user actually see something!

htmlElem = driver.find_element_by_tag_name('html')

htmlElem.send_keys(Keys.ARROW_DOWN)
time.sleep(1)
htmlElem.send_keys(Keys.ARROW_DOWN)
time.sleep(1)
htmlElem.send_keys(Keys.ARROW_DOWN)
time.sleep(1)
htmlElem.send_keys(Keys.ARROW_DOWN)

time.sleep(5)

driver.back()

time.sleep(5)

driver.quit()

# -----------Elements that use the CSS class name-----------
# browser.find_element_by_class_name(name)
# browser.find_elements_by_class_name(name)

# -----------Elements that match the CSS selector-----------
# browser.find_element_by_css_selector(selector)
# browser.find_elements_by_css_selector(selector)

# -----------Elements with a matching id attribute value-----------
# browser.find_element_by_id(id)
# browser.find_elements_by_id(id)

# -----------<a> elements that completely match the text provided-----------
# browser.find_element_by_link_text(text)
# browser.find_elements_by_link_text(text)

# -----------<a> elements that contain the text provided-----------
# browser.find_element_by_partial_link_text(text)
# browser.find_elements_by_partial_link_text(text)

# -----------Elements with a matching name attribute value-----------
# browser.find_element_by_name(name)
# browser.find_elements_by_name(name)

# -----------Elements with a matching tag name (case-insensitive; an <a> element is matched by 'a' and 'A')-----------
# browser.find_element_by_tag_name(name)
# browser.find_elements_by_tag_name(name)