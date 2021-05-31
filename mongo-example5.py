import pymongo

# Insertamos elemento nuevo en la tabla
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

print("-------Insertamos-----------------")
mydict = {"name": "Luis", "address": "Avd de la Ilustracion 18"}

print("Insert realizado")

x = mycol.insert_one(mydict)
print("-------Listamos-----------------")
# Listamos todos los elementos de la tabla
for x in mycol.find():
    print(x)
print("---------Borramos elemento--------")
# Borramos elemento
myquery = {"name": "Luis"}
print("Delete realizado")

mycol.delete_one(myquery)
print("---------Listamos--------------")
# Listamos todos los elementos de la tabla
for x in mycol.find():
    print(x)
