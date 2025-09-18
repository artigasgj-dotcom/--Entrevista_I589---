import Streamlit as tk
from PIL import Image, ImageTk
from entrevista import abrir_entrevista
from parte_a_ampliada import abrir_parte_a_ampliada
from parte_b import abrir_parte_b
from parte_c import abrir_parte_c
from generador_pdf import generar_pdf

def main():
    ventana = tk.Tk()
    ventana.title("Entrevista I-589")
    ventana.geometry("500x600")
    ventana.configure(bg="#f0f4f8")

    # Cargar logo del águila
    try:
        imagen = Image.open("aguila.png")
        imagen = imagen.resize((100, 100), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(imagen)
        ventana.logo = logo  # Mantener referencia para evitar que se borre
        tk.Label(ventana, image=logo, bg="#f0f4f8").pack(pady=10)
    except Exception:
        tk.Label(ventana, text="Formulario I-589", font=("Helvetica", 18, "bold"), bg="#f0f4f8").pack(pady=20)

    # Título simbólico
    tk.Label(
        ventana,
        text="Entrevista con Dignidad",
        font=("Helvetica", 14, "bold"),
        bg="#f0f4f8",
        fg="#003366"
    ).pack(pady=5)

    # Función para crear botones estilizados
    def crear_boton(texto, comando):
        return tk.Button(
            ventana,
            text=texto,
            command=comando,
            font=("Helvetica", 12),
            bg="#ffffff",
            fg="#005b96",
            activebackground="#cce6ff",
            relief="groove",
            bd=2,
            width=30,
            height=2
        )

    # Botones del menú
    botones = [
        ("Parte A - Datos Personales", abrir_entrevista),
        ("Parte A Ampliada", abrir_parte_a_ampliada),
        ("Parte B - Historial Migratorio", abrir_parte_b),
        ("Parte C - Temor y Persecución", abrir_parte_c),
        ("Generar PDF completo", generar_pdf)
    ]

    for texto, funcion in botones:
        crear_boton(texto, funcion).pack(pady=8)

    ventana.mainloop()

if __name__ == "__main__":

    main()
