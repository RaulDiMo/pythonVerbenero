import pymongo

# Insertamos elemento nuevo en la tabla
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

print("---------Borramos elemento--------")
# Borramos elemento
myquery = {"address": "Avd de Bruselas 18"}
print("Delete realizado")

print("-------Insertamos-----------------")
mydict = {"name": "Luis", "address": "Avd de la Ilustracion 18"}

print("Insert realizado")

x = mycol.insert_one(mydict)
print("-------Listamos-----------------")
# Listamos todos los elementos de la tabla
for x in mycol.find():
    print(x)
print("---------Update elemento--------")
# Modificamos elemento
myquery = { "address": "Avd de la Ilustracion 18" }
newvalues = { "$set": { "address": "Avd de Bruselas 18" } }

mycol.update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycol.find():
  print(x)
