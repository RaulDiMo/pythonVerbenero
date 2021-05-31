import pymongo

# Insertamos elementos nuevo en la tabla
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

print("-------Insertamos-----------------")
mydict = {"name": "Juan", "address": "Avd de los Toreros 7"}
x = mycol.insert_one(mydict)
mydict = {"name": "Pablo","address": "Avd de Barcelona 98"}
x = mycol.insert_one(mydict)
mydict = {"name": "Jose","address": "Avd de Cortes 102"}
x = mycol.insert_one(mydict)
mydict = {"name": "Sergio","address": "Calle de Alcala 302"}
x = mycol.insert_one(mydict)
mydict = {"name": "Tomas","address": "Calle Caceres  2"}
x = mycol.insert_one(mydict)
mydict = {"name": "Jesus","address": "Calle Caracas  18"}
x = mycol.insert_one(mydict)
print("Insert realizados")

myresult = mycol.find().limit(5)

#print the result:
for x in myresult:
  print(x)