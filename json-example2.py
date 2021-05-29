import json
#Abrimos fichero externo que contiene un JSON
with open('db.json') as json_data:
# Lo cargamos en una variable diccionario
    d = json.load(json_data)
# Se muestra el contenido por pantalla
    print(d)


