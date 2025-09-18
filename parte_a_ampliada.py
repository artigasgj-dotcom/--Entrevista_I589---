import tkinter as tk
from tkinter import messagebox
from parte_a import crear_base_parte_a, guardar_parte_a_ampliada
import re

def abrir_parte_a_ampliada():
    crear_base_parte_a()

    ventana = tk.Toplevel()
    ventana.title("Parte A Ampliada")
    ventana.geometry("600x600")
    ventana.configure(bg="#f9f9f9")

    campos = {
        "Número A": None,
        "Otros nombres usados": None,
        "Dirección física": None,
        "Dirección postal": None,
        "Nacionalidad actual": None,
        "Nacionalidad de nacimiento": None,
        "Religión": None,
        "Grupo étnico": None,
        "Idiomas hablados": None,
        "Nivel de inglés": None,
        "Estado migratorio actual": None,
        "Número I-94": None
    }

    entradas = {}
    fila = 0
    for etiqueta in campos:
        tk.Label(ventana, text=etiqueta, bg="#f9f9f9").grid(row=fila, column=0, padx=10, pady=5, sticky="w")
        entrada = tk.Entry(ventana, width=50)
        entrada.grid(row=fila, column=1, padx=10, pady=5)
        entradas[etiqueta] = entrada
        fila += 1

    def guardar():
        datos = [entradas[campo].get().strip() for campo in campos]

        numero_a = datos[0]
        numero_i94 = datos[-1]
        nivel_ingles = datos[-3]
        estado_migratorio = datos[-2]

        if not all(datos):
            messagebox.showwarning("Faltan datos", "Por favor completa todos los campos.")
            return

        if not re.match(r"^A\d{8,9}$", numero_a):
            messagebox.showerror("Error", "El número A debe comenzar con 'A' seguido de 8 o 9 dígitos.")
            return

        if not numero_i94.isdigit():
            messagebox.showerror("Error", "El número I-94 debe contener solo dígitos.")
            return

        if re.search(r"[^a-zA-Z\s]", nivel_ingles):
            messagebox.showerror("Error", "El nivel de inglés debe ser una palabra o frase sin números ni símbolos.")
            return

        if re.search(r"[^a-zA-Z\s]", estado_migratorio):
            messagebox.showerror("Error", "El estado migratorio debe ser una palabra o frase sin números ni símbolos.")
            return

        guardar_parte_a_ampliada(*datos)
        messagebox.showinfo("Guardado", "Parte A Ampliada guardada correctamente.")
        ventana.destroy()

    tk.Button(ventana, text="Guardar Parte A Ampliada", command=guardar).grid(row=fila, column=0, columnspan=2, pady=20)