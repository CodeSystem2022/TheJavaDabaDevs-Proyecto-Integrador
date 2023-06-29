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
        
# David Esteche

        # Elimina el socio de la tabla correspondiente
        query = "DELETE FROM socios WHERE nombre = %s"
        value = (nombre_eliminar,)
        cursor.execute(query, value)
        db.commit()

        # Cierra la conexión a la base de datos
        cursor.close()
        db.close()

        # Muestra un mensaje de éxito
        messagebox.showinfo("Eliminación Exitosa", "El socio ha sido eliminado exitosamente.")

        # Limpia el campo de entrada
        entry_eliminar.delete(0, tk.END)
    except mysql.connector.Error as error:
        # Muestra un mensaje de error en caso de que ocurra un problema con la base de datos
        messagebox.showerror("Error de Base de Datos", f"No se pudo eliminar el socio.\nError: {error}")

def mostrar_registros():
    try:
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="1234",
            database="socios"
        )
        cursor = db.cursor()

        # Obtener todos los registros de la tabla socios
        query = "SELECT * FROM socios"
        cursor.execute(query)
        registros = cursor.fetchall()

        # Cierra la conexión a la base de datos
        cursor.close()
        db.close()

        # Crear una nueva ventana para mostrar los registros
        ventana_registros = tk.Toplevel()
        ventana_registros.title("Registros de Socios")

        # Crear un widget de texto para mostrar los registros
        registros_texto = tk.Text(ventana_registros)
        registros_texto.pack()

        # Mostrar los registros en el widget de texto
        for registro in registros:
            registros_texto.insert(tk.END, f"ID: {registro[0]}\nNombre: {registro[1]}\nApellido: {registro[2]}\nDNI: {registro[3]}\n"
                                           f"Dirección: {registro[4]}\nCorreo Electrónico: {registro[5]}\n"
                                           f"Teléfono: {registro[6]}\n\n")

        # Deshabilitar la edición del widget de texto
        registros_texto.configure(state="disabled")

    except mysql.connector.Error as error:
        # Muestra un mensaje de error en caso de que ocurra un problema con la base de datos
        messagebox.showerror("Error de Base de Datos", f"No se pudo mostrar los registros.\nError: {error}")

# Crear ventana principal
window = tk.Tk()
window.title("JavaDabaClub")
window.geometry("400x500")

# Etiquetas y campos de entrada para el registro de socios
label_nombre = tk.Label(window, text="Nombre:")
label_nombre.pack()
entry_nombre = tk.Entry(window)
entry_nombre.pack()

label_apellido = tk.Label(window, text="Apellido:")
label_apellido.pack()
entry_apellido = tk.Entry(window)
entry_apellido.pack()

label_dni = tk.Label(window, text="DNI:")
label_dni.pack()
entry_dni = tk.Entry(window)
entry_dni.pack()

label_direccion = tk.Label(window, text="Dirección:")
label_direccion.pack()
entry_direccion = tk.Entry(window)
entry_direccion.pack()

label_mail = tk.Label(window, text="Correo Electrónico:")
label_mail.pack()
entry_mail = tk.Entry(window)
entry_mail.pack()

label_telefono = tk.Label(window, text="Teléfono:")
label_telefono.pack()
entry_telefono = tk.Entry(window)
entry_telefono.pack()

# Botón para registrar un socio
btn_registrar = tk.Button(window, text="Registrar Socio", command=registrar_socio)
btn_registrar.pack()

# Etiqueta y campo de entrada para buscar un socio por nombre
label_buscar = tk.Label(window, text="Buscar Socio por Nombre:")
label_buscar.pack()
entry_buscar = tk.Entry(window)
entry_buscar.pack()

# Botón para buscar un socio
btn_buscar = tk.Button(window, text="Buscar Socio", command=buscar_socio)
btn_buscar.pack()

# Etiqueta y campo de entrada para eliminar un socio por nombre
label_eliminar = tk.Label(window, text="Eliminar Socio por Nombre:")
label_eliminar.pack()
entry_eliminar = tk.Entry(window)
entry_eliminar.pack()

# Botón para eliminar un socio
btn_eliminar = tk.Button(window, text="Eliminar Socio", command=eliminar_socio)
btn_eliminar.pack()

# Botón para mostrar los registros
btn_mostrar_registros = tk.Button(window, text="Mostrar Registros", command=mostrar_registros)
btn_mostrar_registros.pack()


# Ejecutar ventana principal
window.mainloop()
