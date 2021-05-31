
import requests

#Hacer una petición a una web y mostrarla por pantalla

x = requests.get('https://elpais.com/')

print(x.text)
# Imprime el status de la web
print("Status: " + str(x.status_code))

#Imprime la cabecera
x = requests.head('https://elpais.com/')

print(x.headers)

#Hacer una peticion POST y devolver el texto de respuesta

url = 'https://elpais.com/'
myobj = {'España': 'Sanchez'}

x = requests.post(url, data = myobj)

print(x.text)
