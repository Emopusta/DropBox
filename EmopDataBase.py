import sqlite3

conn = sqlite3.connect('EmopDataBase.db')
cursor = conn.cursor()


cursor.execute(""" SELECT * FROM Users """)
list_all = cursor.fetchall()
print(list_all)
