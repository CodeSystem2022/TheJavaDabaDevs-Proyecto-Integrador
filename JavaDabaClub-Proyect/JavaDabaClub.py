import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Función para registrar un socio en la base de datos
def registrar_socio():
    # Obtiene los datos ingresados por el usuario
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    dni = entry_dni.get()
    direccion = entry_direccion.get()
    mail = entry_mail.get()
    telefono = entry_telefono.get()

 #Código subido por Marcelo
    
 # Limpia los campos de entrada
        entry_nombre.delete(0, tk.END)
        entry_apellido.delete(0, tk.END)
        entry_dni.delete(0, tk.END)
        entry_direccion.delete(0, tk.END)
        entry_mail.delete(0, tk.END)
        entry_telefono.delete(0, tk.END)
    except mysql.connector.Error as error:
        # Muestra un mensaje de error en caso de que ocurra un problema con la base de datos
        messagebox.showerror("Error de Base de Datos", f"No se pudo registrar el socio.\nError: {error}")

# Función para buscar un socio por su nombre en la base de datos
def buscar_socio():
    # Obtiene el nombre ingresado por el usuario
    nombre_buscar = entry_buscar.get()
