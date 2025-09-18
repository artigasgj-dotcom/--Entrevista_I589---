import streamlit as st
import sqlite3

def guardar_parte_c(temor, persecucion, daño, tortura, apoyo):
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS parte_c (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temor TEXT,
            persecucion TEXT,
            daño TEXT,
            tortura TEXT,
            apoyo TEXT
        )
    """)
    cursor.execute("""
        INSERT INTO parte_c (temor, persecucion, daño, tortura, apoyo)
        VALUES (?, ?, ?, ?, ?)
    """, (temor, persecucion, daño, tortura, apoyo))
    conn.commit()
    conn.close()

def abrir_parte_c():
    st.subheader("🧩 Parte C – Temor y Persecución")

    st.markdown("""
    Esta sección recoge tus experiencias de temor, daño y persecución.  
    Puedes compartir con confianza. Tu voz será cuidada con respeto y protección.
    """)

    temor = st.text_area("¿Por qué teme regresar a su país?")
    persecucion = st.text_area("¿Ha sufrido persecución en el pasado?")
    daño = st.text_area("¿Ha recibido amenazas o daño físico?")
    tortura = st.text_area("¿Teme ser torturado si regresa?")
    apoyo = st.text_area("¿Recibe apoyo emocional, legal o espiritual?")

    if st.button("Guardar Parte C"):
        respuestas = [temor, persecucion, daño, tortura, apoyo]

        if not all(respuestas):
            st.warning("⚠️ Por favor completa todos los campos antes de guardar.")
            return

        if any(len(texto.strip()) < 10 for texto in respuestas):
            st.error("❌ Cada respuesta debe tener al menos una frase significativa.")
            return

        guardar_parte_c(*respuestas)
        st.success("✅ Parte C guardada correctamente con dignidad.")
