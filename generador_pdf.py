from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
import sqlite3
from tkinter import messagebox

def generar_pdf():
    try:
        conn = sqlite3.connect("clientes.db")
        cursor = conn.cursor()

        # Parte A básica
        cursor.execute("""
            SELECT nombre, fecha_nacimiento, pais_origen, genero, estado_civil, fecha_entrevista
            FROM clientes ORDER BY id DESC LIMIT 1
        """)
        cliente = cursor.fetchone()

        # Parte A ampliada
        cursor.execute("""
            SELECT numero_a, otros_nombres, direccion_fisica, direccion_postal,
                   nacionalidad_actual, nacionalidad_nacimiento, religion,
                   grupo_etnico, idiomas, nivel_ingles, estado_migratorio, numero_i94
            FROM parte_a_ampliada ORDER BY id DESC LIMIT 1
        """)
        ampliada = cursor.fetchone()

        # Parte B
        cursor.execute("""
            SELECT fecha_entrada, lugar_entrada, modo_entrada, asilo_prev, detenido
            FROM parte_b ORDER BY id DESC LIMIT 1
        """)
        parte_b = cursor.fetchone()

        # Parte C
        cursor.execute("""
            SELECT temor, persecucion, daño, tortura, apoyo
            FROM parte_c ORDER BY id DESC LIMIT 1
        """)
        parte_c = cursor.fetchone()

        conn.close()

        c = canvas.Canvas("I-589_lleno.pdf", pagesize=LETTER)
        c.setFont("Helvetica", 12)
        y = 750

        def seccion(titulo):
            nonlocal y
            c.drawString(50, y, titulo)
            y -= 15
            c.line(50, y, 550, y)
            y -= 20

        def campo(etiqueta, valor):
            nonlocal y
            c.drawString(50, y, f"{etiqueta} {valor}")
            y -= 20

        # Parte A
        if cliente:
            seccion("Parte A - Datos Personales")
            etiquetas = ["Nombre completo", "Fecha de nacimiento", "País de origen", "Género", "Estado civil", "Fecha de entrevista"]
            for etiqueta, valor in zip(etiquetas, cliente):
                campo(etiqueta + ":", valor)

        # Parte A Ampliada
        if ampliada:
            seccion("Parte A Ampliada")
            etiquetas = ["Número A", "Otros nombres", "Dirección física", "Dirección postal",
                         "Nacionalidad actual", "Nacionalidad de nacimiento", "Religión",
                         "Grupo étnico", "Idiomas", "Nivel de inglés", "Estado migratorio", "Número I-94"]
            for etiqueta, valor in zip(etiquetas, ampliada):
                campo(etiqueta + ":", valor)

        # Parte B
        if parte_b:
            seccion("Parte B - Historial Migratorio")
            etiquetas = ["Fecha de entrada", "Lugar de entrada", "Modo de entrada", "¿Solicitó asilo antes?", "¿Fue detenido?"]
            for etiqueta, valor in zip(etiquetas, parte_b):
                campo(etiqueta + ":", valor)

        # Parte C
        if parte_c:
            seccion("Parte C - Temor y Persecución")
            etiquetas = ["Temor al regresar", "Persecución sufrida", "Daño físico recibido", "Temor a tortura", "Apoyo recibido"]
            for etiqueta, valor in zip(etiquetas, parte_c):
                campo(etiqueta + ":", valor)

        c.drawString(50, y - 10, "Este documento fue generado con protección, claridad y dignidad.")
        c.save()

        messagebox.showinfo("PDF generado", "El formulario I-589 fue generado correctamente como 'I-589_lleno.pdf'.")

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo generar el PDF.\n{str(e)}")