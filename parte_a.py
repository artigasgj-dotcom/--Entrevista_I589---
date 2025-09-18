import sqlite3

def crear_base_parte_a():
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS parte_a_ampliada (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_a TEXT,
            otros_nombres TEXT,
            direccion_fisica TEXT,
            direccion_postal TEXT,
            nacionalidad_actual TEXT,
            nacionalidad_nacimiento TEXT,
            religion TEXT,
            grupo_etnico TEXT,
            idiomas TEXT,
            nivel_ingles TEXT,
            estado_migratorio TEXT,
            numero_i94 TEXT
        )
    """)
    conn.commit()
    conn.close()

def guardar_parte_a_ampliada(*datos):
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO parte_a_ampliada (
            numero_a, otros_nombres, direccion_fisica, direccion_postal,
            nacionalidad_actual, nacionalidad_nacimiento, religion,
            grupo_etnico, idiomas, nivel_ingles, estado_migratorio, numero_i94
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, datos)
    conn.commit()
    conn.close()