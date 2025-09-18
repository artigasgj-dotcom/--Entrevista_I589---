import streamlit as st
import sqlite3

def abrir_parte_b():
    st.subheader("📙 Parte B – Historial Migratorio")

    numero_a = st.text_input("Número A del cliente")
    fecha_entrada = st.date_input("Fecha de entrada a EE.UU.")
    lugar_entrada = st.text_input("Lugar de entrada")
    estatus = st.text_input("Estatus migratorio actual")

    if st.button("Guardar Parte B"):
        if not numero_a.strip():
            st.warning("⚠️ Debes ingresar el Número A.")
            return

        try:
            conn = sqlite3.connect("clientes.db")
            cursor = conn.cursor()

            # ⚠️ Solo usar una vez para limpiar la tabla mal creada
            cursor.execute("DROP TABLE IF EXISTS parte_b")

            # Crear tabla correctamente
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS parte_b (
                    numero_a TEXT PRIMARY KEY,
                    fecha_entrada TEXT,
                    lugar_entrada TEXT,
                    estatus_migratorio TEXT
                )
            """)

            # Insertar o actualizar datos
            cursor.execute("""
                INSERT OR REPLACE INTO parte_b (numero_a, fecha_entrada, lugar_entrada, estatus_migratorio)
                VALUES (?, ?, ?, ?)
            """, (numero_a, str(fecha_entrada), lugar_entrada, estatus))

            conn.commit()
            conn.close()
            st.success("✅ Parte B guardada correctamente.")

        except Exception as e:
            st.error(f"❌ Error al guardar los datos: {e}")
