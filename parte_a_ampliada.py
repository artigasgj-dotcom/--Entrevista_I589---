import streamlit as st
import sqlite3

def abrir_parte_a_ampliada():
    st.subheader("📗 Parte A Ampliada – Contacto")

    numero_a = st.text_input("Número A del cliente")
    direccion = st.text_input("Dirección actual")
    telefono = st.text_input("Teléfono")
    correo = st.text_input("Correo electrónico")

    if st.button("Guardar Parte A Ampliada"):
        if not numero_a.strip():
            st.warning("⚠️ Debes ingresar el Número A.")
            return

        try:
            conn = sqlite3.connect("clientes.db")
            cursor = conn.cursor()

            # ⚠️ Solo usar una vez para limpiar la tabla mal creada
            cursor.execute("DROP TABLE IF EXISTS parte_a_ampliada")

            # Crear tabla correctamente
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS parte_a_ampliada (
                    numero_a TEXT PRIMARY KEY,
                    direccion_actual TEXT,
                    telefono TEXT,
                    correo TEXT
                )
            """)

            # Insertar o actualizar datos
            cursor.execute("""
                INSERT OR REPLACE INTO parte_a_ampliada (numero_a, direccion_actual, telefono, correo)
                VALUES (?, ?, ?, ?)
            """, (numero_a, direccion, telefono, correo))

            conn.commit()
            conn.close()
            st.success("✅ Parte A Ampliada guardada correctamente.")

        except Exception as e:
            st.error(f"❌ Error al guardar los datos: {e}")
