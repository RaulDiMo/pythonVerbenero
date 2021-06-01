import mysql.connector

# Conectar base de datos
mydb = mysql.connector.connect(host="localhost",user="root",password="Python")

mycursor = mydb.cursor()

#Mostrar las bases de datos
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)