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
    # Conexión a la base de datos MySQL
    try:
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="1234",
            database="socios"
        )
        cursor = db.cursor()

        # Inserta los datos del socio en la tabla correspondiente
        query = "INSERT INTO socios (nombre, apellido, dni, direccion, mail, telefono) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (nombre, apellido, dni, direccion, mail, telefono)
        cursor.execute(query, values)
        db.commit()

        # Cierra la conexión a la base de datos
        cursor.close()
        db.close()

        # Muestra un mensaje de éxito
        messagebox.showinfo("Registro Exitoso", "El socio ha sido registrado exitosamente.") 

        #Código subido Marcelo
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

# Ciro Valentin Martinez
# Conexión a la base de datos MySQL
    try:
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="1234",
            database="socios"
        )
        cursor = db.cursor()

        # Realiza la búsqueda del socio en la tabla correspondiente
        query = "SELECT * FROM socios WHERE nombre = %s"
        value = (nombre_buscar,)
        cursor.execute(query, value)
        result = cursor.fetchall()

        # Cierra la conexión a la base de datos
        cursor.close()
        db.close()
   # Muestra el resultado de la búsqueda en una ventana emergente
        if result:
            messagebox.showinfo("Búsqueda Exitosa", f"Se encontraron los siguientes socios:\n{result}")
        else:
            messagebox.showinfo("Búsqueda Exitosa", "No se encontraron socios con ese nombre.")
    except mysql.connector.Error as error:
        # Muestra un mensaje de error en caso de que ocurra un problema con la base de datos
        messagebox.showerror("Error de Base de Datos", f"No se pudo realizar la búsqueda.\nError: {error}")
# Función para eliminar un socio de la base de datos
def eliminar_socio():
    # Obtiene el nombre del socio a eliminar
    nombre_eliminar = entry_eliminar.get()

    # Conexión a la base de datos MySQL
    try:
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="1234",
            database="socios"
        )
        cursor = db.cursor()
