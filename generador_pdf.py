import streamlit as st
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from io import BytesIO

def generar_pdf():
    st.subheader("📄 Generador de PDF – Entrevista I-589")

    st.markdown("""
    Este documento reúne tu historia con claridad y dignidad.  
    Puedes generar el archivo para revisión, impresión o entrega.
    """)

    nombre = st.text_input("Nombre completo para el encabezado del PDF")
    resumen = st.text_area("Resumen breve de tu historia (opcional)")

    if st.button("Generar PDF"):
        if not nombre.strip():
            st.warning("⚠️ Por favor ingresa tu nombre antes de generar el PDF.")
            return

        try:
            buffer = BytesIO()
            c = canvas.Canvas(buffer, pagesize=LETTER)
            c.setFont("Helvetica", 12)
            c.drawString(72, 720, f"Entrevista I-589 – {nombre}")
            c.drawString(72, 700, "Resumen:")
            text_obj = c.beginText(72, 680)
            for linea in resumen.split('\n'):
                text_obj.textLine(linea)
            c.drawText(text_obj)
            c.save()

            buffer.seek(0)
            st.success("✅ PDF generado correctamente.")
            st.download_button(
                label="📥 Descargar PDF",
                data=buffer,
                file_name=f"{nombre.replace(' ', '_')}_entrevista.pdf",
                mime="application/pdf"
            )
        except Exception as e:
            st.error(f"❌ Error al generar el PDF: {e}")
