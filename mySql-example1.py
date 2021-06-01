
import mysql.connector

#Conectar base de datos
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Python"
)
#imprimimos base de datos
print(mydb)