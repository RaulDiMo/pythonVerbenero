
import mysql.connector

#Conectar base de datos
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Python",
  database="mydatabase"
)
#Insertar elementos en tabla en mySql

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "Insercion realizada")