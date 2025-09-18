import streamlit as st
import sqlite3

def abrir_entrevista():
    st.subheader("📘 Parte A – Datos Personales")

    # 🧍 Datos del cliente
    numero_a = st.text_input("Número A del cliente")
    nombre = st.text_input("Nombre completo")
    fecha_nacimiento = st.date_input("Fecha de nacimiento")
    pais_origen = st.text_input("País de origen")

    if st.button("Guardar Parte A"):
        if not numero_a.strip():
            st.warning("⚠️ Debes ingresar el Número A para continuar.")
            return

        try:
            conn = sqlite3.connect("clientes.db")
            cursor = conn.cursor()

            # ⚠️ Solo se ejecuta una vez para corregir estructuras previas
            cursor.execute("DROP TABLE IF EXISTS parte_a")

            # 🛠️ Crear tabla con estructura correcta
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS parte_a (
                    numero_a TEXT PRIMARY KEY,
                    nombre TEXT,
                    fecha_nacimiento TEXT,
                    pais_origen TEXT
                )
            """)

            # 💾 Insertar o actualizar datos
            cursor.execute("""
                INSERT OR REPLACE INTO parte_a (numero_a, nombre, fecha_nacimiento, pais_origen)
                VALUES (?, ?, ?, ?)
            """, (numero_a, nombre, str(fecha_nacimiento), pais_origen))

            conn.commit()
            conn.close()
            st.success("✅ Parte A guardada correctamente.")

        except Exception as e:
            st.error(f"❌ Error al guardar los datos: {e}")
