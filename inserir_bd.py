import sqlite3

id = 8
usuario = "junior"
senha = "202122"

banco = sqlite3.connect('elabore.db')

cursor = banco.cursor()

#cursor.execute("CREATE TABLE user (id intereger, usuario text, senha password)")

cursor.execute("INSERT INTO user VALUES('"+str(id)+"','"+usuario+"','"+senha+"')")

#banco.commit()

""" cursor.execute("SELECT * FROM user")
print(cursor.fetchall())  """
