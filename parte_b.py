import streamlit as st

def abrir_parte_b():
    st.subheader("🧩 Parte B – Historial Migratorio")

    st.markdown("""
    Esta sección recoge tu recorrido migratorio.  
    Puedes compartir fechas, lugares y motivos con confianza.  
    Tu historia será tratada con respeto y protección.
    """)

    # Campos migratorios
    fecha_llegada = st.date_input("Fecha de llegada a EE.UU.")
    lugar_ingreso = st.text_input("Lugar de ingreso (puerto/frontera)")
    tipo_entrada = st.selectbox("Tipo de entrada", [
        "Visa de turista", "Visa de trabajo", "Visa de estudiante", "Sin visa", "Otro"
    ])
    detencion = st.radio("¿Fuiste detenido al ingresar?", ["Sí", "No"])
    lugar_detencion = ""
    if detencion == "Sí":
        lugar_detencion = st.text_input("¿Dónde fuiste detenido?")
        documentos_entregados = st.text_area("¿Qué documentos te entregaron durante la detención?")
    else:
        documentos_entregados = st.text_area("¿Qué documentos te entregaron al ingresar?")

    liberacion = st.radio("¿Fuiste liberado con condiciones?", ["Sí", "No"])
    condiciones = ""
    if liberacion == "Sí":
        condiciones = st.text_area("Describe las condiciones de liberación (ej. grillete, presentación, etc.)")

    # Confirmación
    if st.button("Guardar esta sección"):
        st.success("✅ Historial migratorio guardado con dignidad.")
    tk.Button(ventana, text="Guardar Parte B", command=guardar).grid(row=fila, column=0, columnspan=2, pady=20)
