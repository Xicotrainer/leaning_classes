import sqlite3 

conection = sqlite3.connect("DDBB.db")
# To able the conection
querry = conection.cursor()

table = """
	CREATE TABLE books (
		ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
		name VARCHAR(30) NOT NULL,
		autor VARCHAR(40) NOT NULL,
		year INTEGER(9) NOT NULL
		)
	"""
print(table)

if(querry.execute(table)):
	print("A new table was created")
else:
	print("The table was not maded")

querry.close()
conection.commit()
conection.close()