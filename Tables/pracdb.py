import sqlite3
import os

APP_path = os.getcwd()
DB_path = APP_path + "/base.db"

con = sqlite3.connect(DB_path)
con.close()



