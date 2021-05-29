import os

#Comprobamos que el fichero no existe
if os.path.exists("ficheroNuevo.txt"):
# Creamos un fichero. Se tiene que abrir con con el parámetro 'x' de create
    f = open("ficheroNuevo2.txt", "x")
    print("El fichero con ese nombre ya existe le damos otro nombre "+f.name)
else:
# Creamos un fichero. Se tiene que abrir con con el parámetro 'x' de create
    f = open("ficheroNuevo.txt", "x")
    print("El fichero creado..."+f.name)

# Escribimos contenido en el fichero
f.write("Estamos creando un fichero nuevo")

# Cerrar un fichero
f.close()

#Imprimimos lo que contiene el fichero
f = open("ficheroNuevo.txt", "r")

print(f.read())

# Cerrar un fichero
f.close()
