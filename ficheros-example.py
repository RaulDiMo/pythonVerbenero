
#Abrir un fichero con el parámetro 'r' de read
f = open("CrearEntornoVirtual.txt", "r")

f.write("Añadimos más contenido al fichero")

#Imprimimos lo que lee el fichero
print(f.read())

# Cerrar un fichero
f.close()
