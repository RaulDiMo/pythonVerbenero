import json

#Hay que importar la libreria json
# JSON:
x =  '{ "nombre":"Juan", "edad":30, "ciudad":"New York"}'

# Cargamos el Json en una variable python
y = json.loads(x)

# Imprimimos el contenido del Json
print(y)
