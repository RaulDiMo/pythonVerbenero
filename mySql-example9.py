import mysql.connector

# Conectar base de datos
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Python",
    database="mydatabase"
)
#Borrado de elementos en tabla
mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "Filas borradas")