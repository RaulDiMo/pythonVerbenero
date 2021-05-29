
#Abrir un fichero. Se tiene que abrir con con el parámetro 'a' de append
f = open("CrearEntornoVirtual.txt", "a")

f.write("Añadimos más contenido al fichero")

# Cerrar un fichero
f.close()

#Imprimimos lo que contiene el fichero
f = open("CrearEntornoVirtual.txt", "r")

print(f.read())

# Cerrar un fichero
f.close()
