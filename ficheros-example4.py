
import os
#Creamos un fichero. Se tiene que abrir con con el parámetro 'x' de create
f = open("ficheroParaBorrar.txt", "x")

f.write("Estamos creando un fichero nuevo y posteriormente lo vamos a borrar")

# Cerrar un fichero
f.close()

#Imprimimos lo que contiene el fichero
f = open("ficheroParaBorrar.txt", "r")

print(f.read())

# Cerrar un fichero
f.close()

#Comprobamos que existe el fichero antes de borrarlo
if os.path.exists("ficheroParaBorrar.txt"):
# Borrar un fichero.
  os.remove("ficheroParaBorrar.txt")
  print("Atención, el fichero ha sido eliminado....")
else:
  print("El fichero no existe")