
import mysql.connector

#Conectar base de datos
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Python",
  database="mydatabase"
)
#Crear tabla en mySql

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")