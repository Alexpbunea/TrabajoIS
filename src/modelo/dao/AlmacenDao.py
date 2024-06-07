# -*- coding: utf-8 -*-
"""
Created on Fri May  3 13:19:20 2024

@author: Dell XPS 9510
"""

from jaydebeapi import Error
from typing import List
from src.modelo.vo.AlmacenVO import AlmacenVO as Almacen
from src.modelo.conexion.conexionJava import Conexion
from src.modelo.dao.AlmacenInterface import AlmacenInterface

class AlmacenDao(AlmacenInterface, Conexion):
    SQL_SELECT = "SELECT Pieza, Cantidad, PrecioPieza, Concesionario FROM almacen"
    SQL_INSERT = "INSERT INTO almacen (Pieza, Cantidad, PrecioPieza, Concesionario) VALUES (?, ?, ?, ?)"
    SQL_UPDATE = "UPDATE almacen SET Cantidad=?, PrecioPieza=?, Concesionario=? WHERE Pieza=?"
    SQL_DELETE = "DELETE FROM almacen WHERE Pieza=?"

    def getAlmacenes(self) -> List[Almacen]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        almacenes = []

        try:
            if conexion:
                conn = conexion             
            else:
                print("La base de datos no está disponible")            
            cursor = conn.cursor()
            cursor.execute(self.SQL_SELECT)
            rows = cursor.fetchall()
            for row in rows:
                Pieza, Cantidad, PrecioPieza, Concesionario = row
                almacen = Almacen(Pieza, Cantidad, PrecioPieza, Concesionario)
                almacenes.append(almacen)

        except Error as e:
            print("Error al seleccionar almacenes:", e)
        finally:
            if cursor:
                cursor.close()

        conexion = self.close(conn)
        return almacenes

    def insertAlmacen(self, almacen: Almacen) -> int:
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
            cursor.execute(self.SQL_INSERT, (almacen.getPieza(), almacen.getCantidad(), almacen.getPrecioPieza(), almacen.getConcesionario()))
            rows = cursor.rowcount

        except Error as e:
            print("Error al insertar almacen:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.close(conn)
        return rows

    def updateAlmacen(self, almacen: Almacen) -> int:
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
            cursor.execute(self.SQL_UPDATE, (almacen.getCantidad(), almacen.getPrecioPieza(), almacen.getConcesionario(), almacen.getPieza()))
            rows = cursor.rowcount

        except Error as e:
            print("Error al actualizar almacen:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.close(conn)
        return rows

    def deleteAlmacen(self, pieza: str) -> int:
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
            cursor.execute(self.SQL_DELETE, (pieza,))
            rows = cursor.rowcount

        except Error as e:
            print("Error al eliminar almacen:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.close(conn)
        return rows