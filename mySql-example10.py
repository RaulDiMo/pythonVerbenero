import mysql.connector

# Conectar base de datos
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Python",
    database="mydatabase"
)
#Update de elementos en tabla
mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "Registros afectados")