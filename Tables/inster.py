import sqlite3 as sql

def insert():
	db = sql.connect("DDBB.db")
	q = db.cursor()

	print("Please, add a new raw into the table books.\n")

	name = input("Type the novel title: ")
	autor = input("The Autor: ")
	year = input("And the year: ")

	str_values = """\t(
			{},
			{},
			{}
			)""". format(name, autor, year)

	str_inster = """
		INSERT INTO books(
			name,
			autor,
			year
			)
		VALUES 
		"""
	querry = str_inster + str_values
	print(querry)

	q.execute(querry)
	q.close()
	db.commit()
	db.close()


insert()