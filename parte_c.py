import tkinter as tk
from tkinter import messagebox
import sqlite3

def guardar_parte_c(temor, persecucion, daño, tortura, apoyo):
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS parte_c (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temor TEXT,
            persecucion TEXT,
            daño TEXT,
            tortura TEXT,
            apoyo TEXT
        )
    """)
    cursor.execute("""
        INSERT INTO parte_c (temor, persecucion, daño, tortura, apoyo)
        VALUES (?, ?, ?, ?, ?)
    """, (temor, persecucion, daño, tortura, apoyo))
    conn.commit()
    conn.close()

def abrir_parte_c():
    ventana = tk.Toplevel()
    ventana.title("Parte C - Temor y Persecución")
    ventana.geometry("600x500")
    ventana.configure(bg="#f9f9f9")

    campos = {
        "¿Por qué teme regresar a su país?": None,
        "¿Ha sufrido persecución en el pasado?": None,
        "¿Ha recibido amenazas o daño físico?": None,
        "¿Teme ser torturado si regresa?": None,
        "¿Recibe apoyo emocional, legal o espiritual?": None
    }

    entradas = {}
    fila = 0
    for etiqueta in campos:
        tk.Label(ventana, text=etiqueta, bg="#f9f9f9", wraplength=500, justify="left").grid(row=fila, column=0, padx=10, pady=5, sticky="w")
        entrada = tk.Text(ventana, width=60, height=3)
        entrada.grid(row=fila, column=1, padx=10, pady=5)
        entradas[etiqueta] = entrada
        fila += 1

    def guardar():
        datos = [entradas[campo].get("1.0", "end").strip() for campo in campos]

        if not all(datos):
            messagebox.showwarning("Faltan datos", "Por favor completa todos los campos.")
            return

        if any(len(texto) < 10 for texto in datos):
            messagebox.showerror("Error", "Cada respuesta debe tener al menos una frase significativa.")
            return

        guardar_parte_c(*datos)
        messagebox.showinfo("Guardado", "Parte C guardada correctamente.")
        ventana.destroy()

    tk.Button(ventana, text="Guardar Parte C", command=guardar).grid(row=fila, column=0, columnspan=2, pady=20)