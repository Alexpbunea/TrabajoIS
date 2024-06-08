# -*- coding: utf-8 -*-
"""
Created on Fri May  3 13:35:46 2024

@author: Dell XPS 9510
"""

from jaydebeapi import Error
from typing import List
from src.modelo.vo.TallerVO import Taller   
from src.modelo.conexion.conexionJava import Conexion
from src.modelo.dao.TallerInterface import TallerInterface

class TallerDao(TallerInterface, Conexion):
    # Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT IDmaquinaria, Maquinaria, Cantidad, Concesionario FROM taller"
    SQL_INSERT = "INSERT INTO taller (Maquinaria, Cantidad, Concesionario) VALUES (?, ?, ?)"
    SQL_UPDATE = "UPDATE taller SET Maquinaria=?, Cantidad=?, Concesionario=? WHERE IDmaquinaria=?"
    SQL_DELETE = "DELETE FROM taller WHERE IDmaquinaria=?"


    def getTalleres(self) -> List[Taller]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        talleres = []

        try:
            if conexion:
                conn = conexion             
            else:
                print("La base de datos no está disponible")            
            cursor = conn.cursor()
            cursor.execute(self.SQL_SELECT)
            rows = cursor.fetchall()
            for row in rows:
                IDmaquinaria, Maquinaria, Cantidad, Concesionario = row
                taller = Taller(IDmaquinaria, Maquinaria, Cantidad, Concesionario)
                talleres.append(taller)

        except Error as e:
            print("Error al seleccionar talleres:", e)
        finally:
            if cursor:
                cursor.close()

        conexion = self.close(conn)
        return talleres

    def insertTaller(self, taller: Taller) -> int:
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
            cursor.execute(self.SQL_INSERT, (taller.getMaquinaria(), taller.getCantidad(), taller.getConcesionario()))
            rows = cursor.rowcount

        except Error as e:
            print("Error al insertar taller:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.close(conn)
        return rows

    def updateTaller(self, taller: Taller) -> int:
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
            cursor.execute(self.SQL_UPDATE, (taller.getMaquinaria(), taller.getCantidad(), taller.getConcesionario(), taller.getIDmaquinaria()))
            rows = cursor.rowcount

        except Error as e:
            print("Error al actualizar taller:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.close(conn)
        return rows

    def deleteTaller(self, id_maquinaria: int) -> int:
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
            cursor.execute(self.SQL_DELETE, (id_maquinaria,))
            rows = cursor.rowcount

        except Error as e:
            print("Error al eliminar taller:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.close(conn)
        return rows