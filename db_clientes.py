import sqlite3

def crear_base():
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            fecha_nacimiento TEXT,
            pais_origen TEXT,
            genero TEXT,
            estado_civil TEXT,
            fecha_entrevista TEXT
        )
    """)
    conn.commit()
    conn.close()

def guardar_cliente(nombre, fecha_nacimiento, pais_origen, genero, estado_civil, fecha_entrevista):
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO clientes (nombre, fecha_nacimiento, pais_origen, genero, estado_civil, fecha_entrevista)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (nombre, fecha_nacimiento, pais_origen, genero, estado_civil, fecha_entrevista))
    conn.commit()
    conn.close()