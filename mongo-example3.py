
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
print("------------------------------------")
#Seleccionar el primero de la bbdd
x = mycol.find_one()
print(x)
print("------------------------------------")
#Seleccionar todos los elementos de la tabla
for x in mycol.find():
  print(x)
print("------------------------------------")
#Seleccionar columnas de la tabla
for x in mycol.find({},{ "_id": 0, "name":1 }):
  print(x)
