#Pasar un string a un array de varias maneras:
#1) Pensando cada caracter como un elemento del array
#2) Los elementos del array se dividen por espacios en blanco
#3) Utilizando split

coches = "FORD BMW AUDI MERCEDES";

tam=len(coches);

for tam in coches:
	print(tam)

for tam in coches:
	print(" ")
	print(tam)

palabras = coches.split()
for palabra in palabras:
    print (palabra.strip())