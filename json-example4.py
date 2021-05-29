import os
import json
#Abrimos fichero externo que contiene un JSON
with open('db.json') as json_data:
    d = json.load(json_data)

y = json.dumps(d)
#Comprobamos que no existe el fichero, si existe lo borramos
if os.path.exists("fileAJson.txt"):
   os.remove("fileAJson.txt")
#Creamos un fichero para que contenga el contenido del JSON
f = open("fileAJson.txt", "x")
#Grabamos el contenido del Json en el fichero
f.write(y)
#Cerramos el fichero
f.close()


