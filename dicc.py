import unittest
from pprint import pprint

#diccionarios

#Crear un diccionario

dic = {
  "Equipo": "Cadiz",
  "Liga": "Liga Santander",
  "year": 2021
}
print(dic)

    
#Imprimir diccionario

print(dic["Equipo"])

#Conseguir claves

x = dic.keys()
print(x)


#Conseguir Valores

x=dic.values()
print(x)


#añadir valores a un diccionario cuyo un componente es una lista

dicc2 = {"elem1": list(), "elem2": [1, 2, 3]}
dicc2["elem1"].append(1)
dicc2["elem1"].append(2)
print(dicc2)

