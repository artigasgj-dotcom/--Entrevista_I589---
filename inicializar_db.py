import sqlite3

def inicializar_base():
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()

    # Crear Parte A
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS parte_a (
            numero_a TEXT PRIMARY KEY,
            nombre TEXT,
            fecha_nacimiento TEXT,
            pais_origen TEXT
        )
    """)

    # Crear Parte A Ampliada
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS parte_a_ampliada (
            numero_a TEXT PRIMARY KEY,
            direccion_actual TEXT,
            telefono TEXT,
            correo TEXT
        )
    """)

    # Crear Parte B
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS parte_b (
            numero_a TEXT PRIMARY KEY,
            fecha_entrada TEXT,
            lugar_entrada TEXT,
            estatus_migratorio TEXT
        )
    """)

    # Crear Parte C
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS parte_c (
            numero_a TEXT PRIMARY KEY,
            temor TEXT,
            persecucion TEXT,
            daño TEXT,
            tortura TEXT,
            apoyo TEXT
        )
    """)

    conn.commit()
    conn.close()
    print("✅ Base de datos inicializada correctamente.")

# Ejecutar la función al abrir el archivo
inicializar_base()
