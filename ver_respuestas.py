import streamlit as st
import sqlite3

def ver_respuestas():
    st.subheader("🔐 Acceso protegido – Respuestas completas por cliente")

    # Solicitar contraseña
    password = st.text_input("Ingresa la contraseña para acceder", type="password")
    clave_correcta = "prueba2025"

    if password != clave_correcta:
        st.warning("⚠️ Acceso restringido. Ingresa la contraseña correcta para continuar.")
        return

    st.success("✅ Acceso autorizado. Puedes revisar las respuestas guardadas.")

    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()

    # Obtener todos los números A únicos desde parte_a
    try:
        cursor.execute("SELECT DISTINCT numero_a FROM parte_a")
        clientes = cursor.fetchall()
    except Exception as e:
        st.error(f"❌ Error al acceder a los datos: {e}")
        conn.close()
        return

    if not clientes:
        st.info("No hay clientes registrados aún.")
        conn.close()
        return

    for (numero_a,) in clientes:
        with st.expander(f"🧍 Cliente con Número A: {numero_a}"):

            # Parte A – Datos Personales
            cursor.execute("SELECT nombre, fecha_nacimiento, pais_origen FROM parte_a WHERE numero_a = ?", (numero_a,))
            parte_a = cursor.fetchone()
            if parte_a:
                nombre, fecha_nacimiento, pais_origen = parte_a
                st.markdown("### 📘 Parte A – Datos Personales")
                st.markdown(f"- **Nombre completo:** {nombre}")
                st.markdown(f"- **Fecha de nacimiento:** {fecha_nacimiento}")
                st.markdown(f"- **País de origen:** {pais_origen}")

            # Parte A Ampliada
            cursor.execute("SELECT direccion_actual, telefono, correo FROM parte_a_ampliada WHERE numero_a = ?", (numero_a,))
            parte_a_amp = cursor.fetchone()
            if parte_a_amp:
                direccion, telefono, correo = parte_a_amp
                st.markdown("### 📗 Parte A Ampliada")
                st.markdown(f"- **Dirección actual:** {direccion}")
                st.markdown(f"- **Teléfono:** {telefono}")
                st.markdown(f"- **Correo electrónico:** {correo}")

            # Parte B – Historial Migratorio
            cursor.execute("SELECT fecha_entrada, lugar_entrada, estatus_migratorio FROM parte_b WHERE numero_a = ?", (numero_a,))
            parte_b = cursor.fetchone()
            if parte_b:
                fecha_entrada, lugar_entrada, estatus = parte_b
                st.markdown("### 📙 Parte B – Historial Migratorio")
                st.markdown(f"- **Fecha de entrada a EE.UU.:** {fecha_entrada}")
                st.markdown(f"- **Lugar de entrada:** {lugar_entrada}")
                st.markdown(f"- **Estatus migratorio actual:** {estatus}")

            # Parte C – Temor y Persecución
            cursor.execute("SELECT temor, persecucion, daño, tortura, apoyo FROM parte_c WHERE numero_a = ?", (numero_a,))
            parte_c = cursor.fetchone()
            if parte_c:
                temor, persecucion, daño, tortura, apoyo = parte_c
                st.markdown("### 📕 Parte C – Temor y Persecución")
                st.markdown(f"- **¿Por qué teme regresar a su país?**\n{temor}")
                st.markdown(f"- **¿Ha sufrido persecución en el pasado?**\n{persecucion}")
                st.markdown(f"- **¿Ha recibido amenazas o daño físico?**\n{daño}")
                st.markdown(f"- **¿Teme ser torturado si regresa?**\n{tortura}")
                st.markdown(f"- **¿Recibe apoyo emocional, legal o espiritual?**\n{apoyo}")

    conn.close()
