import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

print("-----Busqueda con condicion--------")
#Incluimos una condición de búsqueda
myquery = { "address": "Highway to Hell 99" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)

print("-----Ordenar ascendente--------")
#Ordenar ascendente
mydoc = mycol.find().sort("name")

for x in mydoc:
  print(x)

print("--Ordenar descendente-----")
#Ordenar descendente
mydoc = mycol.find().sort("name", -1)

for x in mydoc:
  print(x)
