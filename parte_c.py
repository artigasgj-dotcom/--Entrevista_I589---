import streamlit as st
import sqlite3

def abrir_parte_c():
    st.subheader("📕 Parte C – Temor y Persecución")

    numero_a = st.text_input("Número A del cliente")
    temor = st.text_area("¿Por qué teme regresar a su país?")
    persecucion = st.text_area("¿Ha sufrido persecución en el pasado?")
    daño = st.text_area("¿Ha recibido amenazas o daño físico?")
    tortura = st.text_area("¿Teme ser torturado si regresa?")
    apoyo = st.text_area("¿Recibe apoyo emocional, legal o espiritual?")

    if st.button("Guardar Parte C"):
        if not numero_a.strip():
            st.warning("⚠️ Debes ingresar el Número A.")
            return

        try:
            conn = sqlite3.connect("clientes.db")
            cursor = conn.cursor()

            # ⚠️ Solo usar una vez para limpiar la tabla mal creada
            cursor.execute("DROP TABLE IF EXISTS parte_c")

            # Crear tabla correctamente
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

            # Insertar o actualizar datos
            cursor.execute("""
                INSERT OR REPLACE INTO parte_c (numero_a, temor, persecucion, daño, tortura, apoyo)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (numero_a, temor, persecucion, daño, tortura, apoyo))

            conn.commit()
            conn.close()
            st.success("✅ Parte C guardada correctamente.")

        except Exception as e:
            st.error(f"❌ Error al guardar los datos: {e}")
