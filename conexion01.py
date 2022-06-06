import sqlite3 as sql3
from sqlite3.dbapi2 import connect

def Crea_DB():
    try:
        conn =sql3.connect("database/"+ mi_db + "sqlite")
        print ("Base de datos creada.")
    except sqlite3.error as error:
        print("Error en sqlite3: ", error)

def Crea_Tabla():
    try:
       Cursor.execute("CREATE TABLE IF NOT EXISTS usuarios(usuarios archar(50), contraseña varchar(50))")
       cnne.commit()
       print("Tabla creada con exito.")
    except sqlite3.error as error:
       print("Error sqlite3 de tabla: ", error)

mi_db = "mi_empresa"
conn =sql3.connect("database/"+ mi_db + "sqlite")
Cursor = conn.cursor()
Crea_Tabla()

Cursor.close()
conn.close ()
