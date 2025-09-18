import streamlit as st
import sqlite3

def ver_respuestas():
    st.subheader("📂 Respuestas Guardadas – Todos los Clientes")

    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()

    # Verificar si la tabla parte_c existe
    cursor.execute("""
        SELECT name FROM sqlite_master 
        WHERE type='table' AND name='parte_c'
    """)
    existe_tabla = cursor.fetchone()

    if not existe_tabla:
        st.info("No hay respuestas guardadas aún en Parte C.")
        conn.close()
        return

    # Obtener todos los registros de parte_c
    cursor.execute("SELECT * FROM parte_c")
    registros = cursor.fetchall()

    if registros:
        st.markdown("### 🧾 Parte C – Temor y Persecución")
        for registro in registros:
            id_, temor, persecucion, daño, tortura, apoyo = registro
            with st.expander(f"🧍 Cliente #{id_}"):
                st.markdown(f"**¿Por qué teme regresar a su país?**  
                {temor}")
                st.markdown(f"**¿Ha sufrido persecución en el pasado?**  
                {persecucion}")
                st.markdown(f"**¿Ha recibido amenazas o daño físico?**  
                {daño}")
                st.markdown(f"**¿Teme ser torturado si regresa?**  
                {tortura}")
                st.markdown(f"**¿Recibe apoyo emocional, legal o espiritual?**  
                {apoyo}")
    else:
        st.info("No hay respuestas registradas en Parte C aún.")

    conn.close()
