# -*- coding: utf-8 -*-
"""
Created on Fri May  3 13:19:20 2024

@author: Dell XPS 9510
"""

from jaydebeapi import Error
from typing import List
from src.modelo.vo.AlmacenVO import AlmacenVO
from src.modelo.conexion.conexionJava import Conexion
from src.modelo.dao.AlmacenInterface import AlmacenInterface

class AlmacenDao(AlmacenInterface, Conexion):
    # Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT capacidad, piezas FROM Almacen"
    SQL_INSERT = "INSERT INTO Almacen(capacidad, piezas) VALUES (?, ?)"

    def getAlmacenes(self) -> List[AlmacenVO]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        almacenes = []

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
                capacidad, piezas = row
                # Crea un objeto AlmacenVO para cada fila
                almacen = AlmacenVO()
                almacen.setCapacidad(capacidad)
                almacen.setPiezas(piezas)
                almacenes.append(almacen)

        except Error as e:
            print("Error al seleccionar almacenes:", e)
        # Se ejecuta siempre
        finally:
            if cursor:
                # Cierra el cursor para liberar recursos
                cursor.close()

        conexion = self.closeConnection(conn)
        return almacenes
    

    def insertAlmacen(self, almacen: AlmacenVO) -> int:
        conexion = self.getConnection()
        conn = None
        cursor = None
        rows = 0

        try:
            if conexion:
                conn = conexion 
            
            else:
                print("La base de datos no esta disponible")
            cursor = conn.cursor()
            cursor.execute(self.SQL_INSERT, (almacen.getCapacidad(), almacen.getPiezas()))
            
            rows = cursor.rowcount

        except Error as e:
            print("Error al insertar almacén:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows
