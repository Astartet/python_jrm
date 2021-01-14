import mysql.connector as mysql

db = mysql.connect(
    host ="localhost",
    user = "root",
    passwd = "armado12",
    database = "prueba"
)

cursor = db.cursor()

cursor.execute("DESC formulario")
print(cursor.fetchall())