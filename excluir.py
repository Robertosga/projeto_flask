import sqlite3
try:
    banco = sqlite3.connect('elabore.db')

    cursor = banco.cursor()

    #cursor.execute("DELETE From user WHERE id = 5")

    banco.commit()
    banco.close()
    print("os dados foram removidos com sucesso!!")

except sqlite3.Error as erro:
    print("Erro ao excluir:",erro)