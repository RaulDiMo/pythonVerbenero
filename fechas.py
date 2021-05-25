#Usando las funcionalidades de date. Escribir un ejercicio python que imprima el día de hoy, el año y el mes
#Después que imprima hora y minuto

import datetime

x = datetime.datetime.now()
print("Fecha:")
print(x)
print("Dia de la semana: ")
print(x.strftime("%A"))
print("Dia: ")
print(x.strftime("%d"))
print("Mes: ")
print(x.strftime("%B"))
print("Year: ")
print(x.strftime("%Y"))
print("Hora: ")
print(x.strftime("%H"))
print("Minuto: ")
print(x.strftime("%M"))
print("Segundo: ")
print(x.strftime("%S"))
print("Dia del año: ")
print(x.strftime("%j"))