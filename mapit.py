import webbrowser, pyperclip

address = input("Ingrese la dirección que desea buscar (si quiere importar desde el porta papeles, presione ENTER): ")
if address:
    address = address.replace(' ', '+')
else:    
    address = pyperclip.paste().replace(' ', '+')
webbrowser.open("https://maps.google.com/maps/place/" + address)