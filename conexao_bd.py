import sqlite3
from sqlite3 import Error

def ConexaoBanco():
    caminho= "elabore.db"
    con =None
    try:
        con=sqlite3.connect(caminho)

    except Error as ex:
        print(ex)
    return con


