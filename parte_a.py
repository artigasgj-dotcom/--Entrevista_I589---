import streamlit as st
import sqlite3

def abrir_entrevista():
    st.subheader("🧩 Parte A – Datos Personales")
    st.markdown("Esta sección honra tu identidad.\nResponde con calma y claridad.\nTu información será tratada con respeto y protección.")

    numero_a = st.text_input("🆔 Número A del cliente (obligatorio)")
    nombre = st.text_input("Nombre completo")
    fecha_nacimiento = st.date_input("Fecha de nacimiento")
    pais_origen = st.text_input("País de origen")
    idioma = st.text_input("Idioma principal")
    direccion = st.text_input("Dirección actual")
    telefono = st.text_input("Teléfono de contacto")
    correo = st.text_input("Correo electrónico")
    genero = st.selectbox("Identidad de género", ["Masculino", "Femenino", "Otro", "Prefiero no decir"])
    estado_civil = st.selectbox("Estado civil", ["Soltero/a", "Casado/a", "Separado/a", "Viudo/a", "Otro"])

    if st.button("Guardar Parte A"):
        if not numero_a.strip():
            st.warning("⚠️ Debes ingresar el Número A para continuar.")
            return

        try:
            conn = sqlite3.connect("clientes.db")
            cursor = conn.cursor()

            # Crear tabla si no existe
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS parte_a (
                    numero_a TEXT PRIMARY KEY,
                    nombre TEXT,
                    fecha_nacimiento TEXT,
                    pais_origen TEXT,
                    idioma TEXT,
                    direccion TEXT,
                    telefono TEXT,
                    correo TEXT,
                    genero TEXT,
                    estado_civil TEXT
                )
            """)

            # Insertar o actualizar datos
            cursor.execute("""
                INSERT OR REPLACE INTO parte_a (
                    numero_a, nombre, fecha_nacimiento, pais_origen,
                    idioma, direccion, telefono, correo, genero, estado_civil
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                numero_a, nombre, str(fecha_nacimiento), pais_origen,
                idioma, direccion, telefono, correo, genero, estado_civil
            ))

            conn.commit()
            conn.close()
            st.success("✅ Parte A guardada correctamente.")

        except Exception as e:
            st.error(f"❌ Error al guardar los datos: {e}")
