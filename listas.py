import unittest
from pprint import pprint

#Crear una lista

lista = ["manzana", "platano", "cereza"]

print(lista)

# Añadir elementos a la lista
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)

print(mylist);

# Cambiar un elemento

lista = ["manzana", "platano", "cereza"]
lista[1] = "coco"
print(lista)


#Eliminar un elemento

lista = ["manzana", "platano", "cereza"]
lista.remove("cereza")
print(lista)

#Eliminar un determinado elemento

lista = ["manzana", "platano", "cereza"]
lista.pop(1)
print(lista)

#Ordenar listas

lista = [100, 50, 65, 82, 23]
lista.sort()
print(lista)

#Ordernar listas descendente

lista = [100, 50, 65, 82, 23]
lista.sort(reverse = True)
print(lista)







