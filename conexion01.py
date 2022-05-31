import sqlite3 as sql3

def Crea_Tabla():
Cursor.execute("CREATE TABLE IF NOT EXISTS usuarios(usuarios(
 varchar, contraseña varchar)")
Cursor.commit()
print("Tabla creada con exito.")

mi_db = "mi_empresa"
conn =sql3.connect("database/"+ + mi_db +"sqlite")
Cursor = conn.cursor()

try:
    Crea_Tabla()
except Exception as ex:
    print ("Error de excepción: " + e)

Cursor.close()
