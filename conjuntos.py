import unittest
from pprint import pprint

#Crear un Conjuntos

conjunto = {"leche", "pan", "agua"}
print(conjunto)


#Añadir al conjunto

conjunto.add("orange")

print(conjunto)


#Concatenar conjuntos

conjunto2 ={"arroz","tomate","lechuga"}

conjunto.update(conjunto2)

print(conjunto)

#Eliminar un elemento de un conjunto
 
        
conjunto.remove("tomate")
print(conjunto)        
        