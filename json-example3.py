import json

# Creamos un diccionario en python
x = {
  "nombre": "Juan",
  "edad": 12,
  "asignatura": "Matematicas",
  "Calificacion": 7.5
}

# Lo convertimos en json
y = json.dumps(x)

# Imprimos el resultado
print(y)


