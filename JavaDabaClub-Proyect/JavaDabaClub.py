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
