import mysql.connector

# Conectar base de datos
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Python",
    database="mydatabase"
)
mycursor = mydb.cursor()

# Select a tabla mySql
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
print("--------------------------------------")
# Select por columna a tabla
mycursor = mydb.cursor()

mycursor.execute("SELECT name FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
   print(x)
print("--------------------------------------")
# Select con filtro
mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
   print(x)

print("--------------------------------------")
# Select con order by
mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name desc"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

print("--------------------------------------")
# Select con limit
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)