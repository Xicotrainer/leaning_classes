import sqlite3
import os

APP_path = os.getcwd()
DB_path = APP_path + "/base.db"

con = sqlite3.connect(DB_path)
cursor = con.cursor()

cursor.execute(
	"""
	CREATE TABLE users_(
		ID		INT		PRIMARY KEY		NOT NULL,
		name	TEXT 					NOT NULL,
		age		INT,
		status 	BIT 					NOT NULL
		)
	"""
	)

con.close()