import streamlit as st

def abrir_entrevista():
    st.subheader("🧩 Parte A – Datos Personales")

    st.markdown("""
    Esta sección honra tu identidad.  
    Responde con calma y claridad.  
    Tu información será tratada con respeto y protección.
    """)

    # Campos básicos
    nombre = st.text_input("Nombre completo")
    fecha_nacimiento = st.date_input("Fecha de nacimiento")
    pais_origen = st.text_input("País de origen")
    idioma = st.text_input("Idioma principal")
    direccion = st.text_area("Dirección actual")

    # Campos opcionales
    telefono = st.text_input("Teléfono de contacto")
    correo = st.text_input("Correo electrónico")
    genero = st.selectbox("Identidad de género", ["Masculino", "Femenino", "No binario", "Prefiero no decir", "Otro"])
    estado_civil = st.selectbox("Estado civil", ["Soltero/a", "Casado/a", "Separado/a", "Viudo/a", "Otro"])

    # Confirmación
    if st.button("Guardar esta sección"):
        st.success("✅ Datos personales guardados con dignidad.")
