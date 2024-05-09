# -*- coding: utf-8 -*-
"""
Created on Fri May  3 13:25:16 2024

@author: Dell XPS 9510
"""

from jaydebeapi import Error
from typing import List
from src.modelo.vo.JefeZonaVO import JefeZona
from src.modelo.conexion.conexionJava import Conexion
from src.modelo.dao.JefeZonaInterface import JefeZonaInterface

class JefeZonaDao(JefeZonaInterface, Conexion):
    # Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT IDjefeZona FROM JefesZona"
    SQL_INSERT = "INSERT INTO JefesZona(IDjefeZona) VALUES (?)"

    def getJefesZona(self) -> List[JefeZona]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        jefes_zona = []

        try:
            if conexion:
                conn = conexion             
            else:
                print("La base de datos no esta disponible")            
            # Crea un objeto para poder ejecutar consultas SQL sobre la conexion abierta
            cursor = conn.cursor()
            # Ejecuta la consulta SQL
            cursor.execute(self.SQL_SELECT)
            # Obtiene todas las filas resultantes de la consulta
            rows = cursor.fetchall()
            # Itera sobre todas las filas
            for row in rows:
                IDjefeZona, = row  # Se utiliza la coma para desempaquetar la tupla
                # Crea un objeto JefeZona para cada fila
                jefe_zona = JefeZona()
                jefe_zona.setIDjefeZona(IDjefeZona)
                jefes_zona.append(jefe_zona)

        except Error as e:
            print("Error al seleccionar jefes de zona:", e)
        # Se ejecuta siempre
        finally:
            if cursor:
                # Cierra el cursor para liberar recursos
                cursor.close()

        conexion = self.closeConnection(conn)
        return jefes_zona
    

    def insertJefeZona(self, jefe_zona: JefeZona) -> int:
        conexion = self.getConnection()
        conn = None
        cursor = None
        rows = 0

        try:
            if conexion:
                conn = conexion 
            
            else:
                print("La base de datos no está disponible")
            cursor = conn.cursor()
            cursor.execute(self.SQL_INSERT, (jefe_zona.getIDjefeZona(),))
            
            rows = cursor.rowcount

        except Error as e:
            print("Error al insertar jefe de zona:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows
