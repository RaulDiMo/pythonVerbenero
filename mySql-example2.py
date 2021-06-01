import mysql.connector

# Conectar base de datos
mydb = mysql.connector.connect(host="localhost",user="root",password="Python")
mycursor = mydb.cursor()
# Crear base de datos
mycursor.execute("CREATE DATABASE mydatabase")
