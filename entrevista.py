import tkinter as tk
from tkinter import messagebox
from db_clientes import crear_base, guardar_cliente
import re

def abrir_entrevista():
    crear_base()  # Asegura que la tabla 'clientes' exista

    ventana = tk.Toplevel()
    ventana.title("Parte A - Datos Personales")
    ventana.geometry("500x400")
    ventana.configure(bg="#f9f9f9")

    campos = {
        "Nombre completo": None,
        "Fecha de nacimiento (AAAA-MM-DD)": None,
        "País de origen": None,
        "Género": None,
        "Estado civil": None,
        "Fecha de entrevista (AAAA-MM-DD)": None
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

        nombre = datos[0]
        fecha_nacimiento = datos[1]
        fecha_entrevista = datos[5]

        # Validaciones
        if not all(datos):
            messagebox.showwarning("Faltan datos", "Por favor completa todos los campos.")
            return

        if not re.match(r"^\d{4}-\d{2}-\d{2}$", fecha_nacimiento):
            messagebox.showerror("Error", "La fecha de nacimiento debe tener el formato AAAA-MM-DD.")
            return

        if not re.match(r"^\d{4}-\d{2}-\d{2}$", fecha_entrevista):
            messagebox.showerror("Error", "La fecha de entrevista debe tener el formato AAAA-MM-DD.")
            return

        if re.search(r"\d", nombre):
            messagebox.showerror("Error", "El nombre no debe contener números.")
            return

        guardar_cliente(*datos)
        messagebox.showinfo("Guardado", "Datos personales guardados correctamente.")
        ventana.destroy()

    tk.Button(ventana, text="Guardar Parte A", command=guardar).grid(row=fila, column=0, columnspan=2, pady=20)