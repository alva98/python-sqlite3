import sqlite3 as sql3

mi_db = "mi_empresa"

conn =sql3.connect("database/"+ + mi_db +"sqlite")
Cursor = conn.cursor()

try:
    Crea_Tabla()
except Exception as ex:
    print ("Error de excepción: " + e)

Cursor.close()
