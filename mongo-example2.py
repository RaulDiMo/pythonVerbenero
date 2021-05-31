
import pymongo

#Insertamos elementos en la tabla
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydict = { "name": "Pedro", "address": "Highway to Hell 99" }

x = mycol.insert_one(mydict)

