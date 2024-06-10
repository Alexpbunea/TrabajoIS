# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import subprocess
import tkinter as tk
from tkinter import messagebox, filedialog
import datetime
import jaydebeapi

class Conexion:

    # Especifica los detalles de la conexión
    host = 'localhost'
    database = 'datoscofermotor'
    user = 'root'
    password = 'changeme'

    "Abre una conexión a la base de datos."
    @staticmethod
    def getConnection():
        try:
            # Cargar el driver JDBC de MySQL
            jdbc_driver = "com.mysql.cj.jdbc.Driver"
            jar_file = "./lib/mysql-connector-j-8.3.0.jar"
            return jaydebeapi.connect(jdbc_driver, f"jdbc:mysql://{Conexion.host}/{Conexion.database}", [Conexion.user, Conexion.password], jar_file)
        except Exception as e:
            print(e)
            return None

    "Cierra una conexión a la base de datos."
    @staticmethod
    def close(conn):
        try:
            conn.close()
        except Exception as e:
            print(e)
  
            
def realizar_copia_seguridad():
    conn = Conexion.getConnection()
    if conn is None:
        messagebox.showerror("Error", "No se pudo conectar a la base de datos.")
        return

    # Pedir al usuario que seleccione la carpeta para guardar la copia de seguridad
    ruta_carpeta = filedialog.askdirectory()
    if not ruta_carpeta:
        Conexion.close(conn)
        return  # El usuario canceló la selección

    # Parámetros de la base de datos
    host = Conexion.host
    user = Conexion.user
    password = Conexion.password
    db_name = Conexion.database

    # Nombre del archivo de la copia de seguridad
    fecha_actual = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"{ruta_carpeta}/backup_{db_name}_{fecha_actual}.sql"

    # Comando mysqldump
    comando = f"mysqldump -h {host} -u {user} -p{password} {db_name} > {backup_file}"

    try:
        # Ejecutar el comando mysqldump
        subprocess.run(comando, shell=True, check=True)
        messagebox.showinfo("Éxito", f"Copia de seguridad realizada correctamente.\nArchivo: {backup_file}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error al realizar la copia de seguridad:\n{e}")
    finally:
        Conexion.close(conn)

# Crear la interfaz gráfica
#root = tk.Tk()
#root.title("Copia de Seguridad MySQL")
#Sroot.geometry("400x200")

#boton_copia = tk.Button(root, text="Realizar Copia de Seguridad", command=realizar_copia_seguridad)
#boton_copia.pack(pady=20)

#root.mainloop()




