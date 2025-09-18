import tkinter as tk
from tkinter import messagebox
import sqlite3
import re

def guardar_parte_b(fecha_entrada, lugar_entrada, modo_entrada, asilo_prev, detenido):
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS parte_b (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha_entrada TEXT,
            lugar_entrada TEXT,
            modo_entrada TEXT,
            asilo_prev TEXT,
            detenido TEXT
        )
    """)
    cursor.execute("""
        INSERT INTO parte_b (fecha_entrada, lugar_entrada, modo_entrada, asilo_prev, detenido)
        VALUES (?, ?, ?, ?, ?)
    """, (fecha_entrada, lugar_entrada, modo_entrada, asilo_prev, detenido))
    conn.commit()
    conn.close()

def abrir_parte_b():
    ventana = tk.Toplevel()
    ventana.title("Parte B - Historial Migratorio")
    ventana.geometry("500x400")
    ventana.configure(bg="#f9f9f9")

    campos = {
        "Fecha de entrada (AAAA-MM-DD)": None,
        "Lugar de entrada": None,
        "Modo de entrada (visa, frontera, etc.)": None,
        "¿Solicitó asilo antes? (Sí/No)": None,
        "¿Fue detenido por inmigración? (Sí/No)": None
    }

    entradas = {}
    fila = 0
    for etiqueta in campos:
        tk.Label(ventana, text=etiqueta, bg="#f9f9f9").grid(row=fila, column=0, padx=10, pady=5, sticky="w")
        entrada = tk.Entry(ventana, width=40)
        entrada.grid(row=fila, column=1, padx=10, pady=5)
        entradas[etiqueta] = entrada
        fila += 1

    def guardar():
        datos = [entradas[campo].get().strip() for campo in campos]

        fecha_entrada = datos[0]
        modo_entrada = datos[2]
        asilo_prev = datos[3].lower()
        detenido = datos[4].lower()

        if not all(datos):
            messagebox.showwarning("Faltan datos", "Por favor completa todos los campos.")
            return

        if not re.match(r"^\d{4}-\d{2}-\d{2}$", fecha_entrada):
            messagebox.showerror("Error", "La fecha de entrada debe tener el formato AAAA-MM-DD.")
            return

        if asilo_prev not in ["sí", "no"]:
            messagebox.showerror("Error", "La respuesta a '¿Solicitó asilo antes?' debe ser 'Sí' o 'No'.")
            return

        if detenido not in ["sí", "no"]:
            messagebox.showerror("Error", "La respuesta a '¿Fue detenido?' debe ser 'Sí' o 'No'.")
            return

        if re.search(r"[^\w\s]", modo_entrada):
            messagebox.showerror("Error", "El modo de entrada no debe contener símbolos.")
            return

        guardar_parte_b(*datos)
        messagebox.showinfo("Guardado", "Parte B guardada correctamente.")
        ventana.destroy()

    tk.Button(ventana, text="Guardar Parte B", command=guardar).grid(row=fila, column=0, columnspan=2, pady=20)