import mysql.connector as mysql

db = mysql.connect(
    host ="localhost",
    user = "root",
    passwd = "armado12",
    database = "prueba"
)

cursor = db.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS form (nombre VARCHAR(30), ciudad VARCHAR(30))")
query = "INSERT INTO form VALUES (%s,%s)"
values =("jorge","sevilla")
cursor.execute(query,values)

db.commit()
print(cursor.rowcount, "record inserted")