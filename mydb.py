import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'password',

	)

# prepare a cursor obj
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE base")

print("done")