# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import jaydebeapi

class Conexion:

    # Especifica los detalles de la conexión
    host = 'localhost'
    database = 'DatosCoferMotor'
    user = 'root'
    password = 'changeme'

    "Abre una conexión a la base de datos."
    @staticmethod
    def getConnection():
        try:
            # Cargar el driver JDBC de MySQL
            jdbc_driver = "com.mysql.cj.jdbc.Driver"
            jar_file = "lib/mysql-connector-j-8.3.0.jar"
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
  
            
a = Conexion.getConnection()
print(a)
Conexion.close(a)