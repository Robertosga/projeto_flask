import sqlite3

banco = sqlite3.connect('elabore.db')

cursor = banco.cursor()


cursor.execute("UPDATE user SET usuario = 'Maria' WHERE id = 5")

#banco.commit()

""" cursor.execute("SELECT * FROM user")
print(cursor.fetchall())  """
