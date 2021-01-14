import mysql.connector as mysql
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "armado12"
)
#print(db)

cursor = db.cursor()

cursor.execute("CREATE DATABASE prueba")
