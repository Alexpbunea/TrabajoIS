# -*- coding: utf-8 -*-
"""
Created on Fri May  3 13:20:55 2024

@author: Dell XPS 9510
"""

from jaydebeapi import Error
from typing import List
from src.modelo.vo.ConcesionarioVO import Concesionario
from src.modelo.conexion.conexionJava import Conexion
from src.modelo.dao.ConcesionarioInterface import ConcesionarioInterface

class ConcesionarioDao(ConcesionarioInterface, Conexion):
    # Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT Nombre, Direccion, Ciudad, FechaInauguracion FROM Concesionario"
    SQL_INSERT = "INSERT INTO Concesionario(Nombre, Direccion, Ciudad, FechaInauguracion) VALUES (?, ?, ?, ?)"
    SQL_DELETE = "DELETE FROM Concesionario WHERE Nombre = ?"
    SQL_UPDATE = "UPDATE Concesionario SET Direccion = ?, Ciudad = ?, FechaInauguracion = ? WHERE Nombre = ?"

    def getConcesionarios(self) -> List[Concesionario]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        concesionarios = []

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
                nombre, direccion, ciudad, fecha_inauguracion = row
                # Crea un objeto Concesionario para cada fila
                concesionario = Concesionario()
                concesionario.setNombre(nombre)
                concesionario.setDireccion(direccion)
                concesionario.setCiudad(ciudad)
                concesionario.setFechaInauguracion(fecha_inauguracion)
                concesionarios.append(concesionario)

        except Error as e:
            print("Error al seleccionar concesionarios:", e)
        # Se ejecuta siempre
        finally:
            if cursor:
                # Cierra el cursor para liberar recursos
                cursor.close()

        conexion = self.close(conn)
        return concesionarios
    

    def insertConcesionario(self, concesionario: Concesionario) -> int:
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
            cursor.execute(self.SQL_INSERT, (concesionario.getNombre(), concesionario.getDireccion(), concesionario.getCiudad(), concesionario.getFechaInauguracion()))
            
            rows = cursor.rowcount

        except Error as e:
            print("Error al insertar concesionario:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.close(conn)

        return rows

    def deleteConcesionario(self, nombre: str) -> int:
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
            cursor.execute(self.SQL_DELETE, (nombre,))
            rows = cursor.rowcount

        except Error as e:
            print("Error al eliminar concesionario:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.close(conn)
        return rows

    def updateConcesionario(self, concesionario: Concesionario) -> int:
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
            cursor.execute(self.SQL_UPDATE, (concesionario.getDireccion(), concesionario.getCiudad(), concesionario.getFechaInauguracion(), concesionario.getNombre()))
            rows = cursor.rowcount

        except Error as e:
            print("Error al actualizar concesionario:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.close(conn)
        return rows