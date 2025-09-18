import streamlit as st
from PIL import Image

# Importar módulos funcionales
from entrevista import abrir_entrevista
from parte_a_ampliada import abrir_parte_a_ampliada
from parte_b import abrir_parte_b
from parte_c import abrir_parte_c
from generador_pdf import generar_pdf
from ver_respuestas import ver_respuestas  # Nuevo módulo agregado

# 🦅 Configuración de la página
st.set_page_config(page_title="Entrevista Ética I-589", page_icon="🦅", layout="centered")

# 🛡️ Encabezado ceremonial
st.title("🦅 Entrevista con Dignidad")
st.markdown("""
Este espacio honra tu historia.  
Cada respuesta será tratada con respeto, protección y propósito.
""")

# 🖼️ Mostrar imagen del águila
try:
    imagen = Image.open("aguila.png.png")
    st.image(imagen, caption="Símbolo de protección", use_container_width=True)
except Exception:
    st.subheader("Formulario I-589")

# 📋 Menú de navegación
opcion = st.selectbox("Selecciona una sección:", [
    "Parte A - Datos Personales",
    "Parte A Ampliada",
    "Parte B - Historial Migratorio",
    "Parte C - Temor y Persecución",
    "Generar PDF completo",
    "Ver respuestas guardadas"  # Nueva opción agregada
])

# 🔄 Ejecutar función correspondiente
if opcion == "Parte A - Datos Personales":
    abrir_entrevista()
elif opcion == "Parte A Ampliada":
    abrir_parte_a_ampliada()
elif opcion == "Parte B - Historial Migratorio":
    abrir_parte_b()
elif opcion == "Parte C - Temor y Persecución":
    abrir_parte_c()
elif opcion == "Generar PDF completo":
    generar_pdf()
elif opcion == "Ver respuestas guardadas":
    ver_respuestas()

# 🧭 Pie de página ceremonial
st.markdown("---")
st.markdown("""
Aplicación creada por Jorge Artigas  
para proteger la voz de quienes buscan asilo.  
Diseñada con claridad, dignidad y propósito.
""")


