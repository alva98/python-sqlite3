import sqlite3 as sql3

def Crea_DB():
    try:
        conn =sql3.connect("database/"+ mi_db + "sqlite")
        conn =sql3.connect("database/"+ mi_db + "sqlite")
        Mantén pulsado un clip para fijarlo. Los clips no fijados se eliminarán al cabo de una hora.conn =sql3.connect("database/"+ mi_db + "sqlite")
conn =sql3.connect("database/"+ mi_db + "sqlite")
Mantén pulsado un clip paa ijarlo. Los clips no fijados se eliminarán al cabo de una hh

def Crea_Tabla():

Cursor.execute("CREATE TABLE IF NOT EXISTS usuarios(usuarios
 varchar(50), contraseña varchar(50))")
Cursor.commit()
print("Tabla creada con exito.")

mi_db = "mi_empresa"
conn =sql3.connect("database/"+ mi_db + "sqlite")
Cursor = conn.cursor()

def Crea_Tabla()

try:
    Crea_Tabla()
except Exception as ex:
    print ("Error de excepción: " + e)

Cursor.close()
