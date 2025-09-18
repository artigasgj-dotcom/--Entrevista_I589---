import streamlit as st

def abrir_parte_a_ampliada():
    st.subheader("🧩 Parte A Ampliada – Detalles de Identidad")

    st.markdown("""
    Esta sección amplía tu historia personal.  
    Puedes compartir detalles que ayuden a comprender tu contexto con claridad y respeto.  
    Tu voz será cuidada con dignidad.
    """)

    # Campos ampliados
    ocupacion = st.text_input("Ocupación actual")
    nivel_educativo = st.selectbox("Nivel educativo", [
        "Sin escolaridad", "Primaria", "Secundaria", "Técnico", "Universitario", "Otro"
    ])
    grupo_etnico = st.text_input("Grupo étnico o cultural")
    religion = st.text_input("Religión o práctica espiritual")
    identidad_comunitaria = st.text_area("¿Cómo te identificas dentro de tu comunidad?")
    idioma_secundario = st.text_input("¿Hablas otro idioma además del principal?")
    habilidades = st.text_area("¿Qué habilidades o conocimientos consideras valiosos?")
    contexto_familiar = st.text_area("¿Hay algo que debamos saber sobre tu familia o entorno?")
    valores_personales = st.text_area("¿Qué valores te guían en tu vida diaria?")

    # Confirmación
    if st.button("Guardar esta sección"):
        st.success("✅ Parte A Ampliada guardada con dignidad.")
