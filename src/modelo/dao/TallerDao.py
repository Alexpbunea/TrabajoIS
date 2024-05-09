# -*- coding: utf-8 -*-
"""
Created on Fri May  3 13:35:46 2024

@author: Dell XPS 9510
"""

from jaydebeapi import Error
from typing import List
from src.modelo.vo.Taller import Taller
from src.modelo.conexion.conexionJava import Conexion
from src.modelo.dao.TallerInterface import TallerInterface

class TallerDao(TallerInterface, Conexion):
    # Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT horario, Maquinaria, Concesionario FROM Talleres"
    SQL_INSERT = "INSERT INTO Talleres(horario, Maquinaria, Concesionario) VALUES (?, ?, ?)"

    def getTalleres(self) -> List[Taller]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        talleres = []

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
                horario, Maquinaria, Concesionario = row
                # Crea un objeto Taller para cada fila
                taller = Taller()
                taller.setHorario(horario)
                taller.setMaquinaria(Maquinaria)
                taller.setConcesionario(Concesionario)
                talleres.append(taller)

        except Error as e:
            print("Error al seleccionar talleres:", e)
        # Se ejecuta siempre
        finally:
            if cursor:
                # Cierra el cursor para liberar recursos
                cursor.close()

        conexion = self.closeConnection(conn)
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
                print("La base de datos no esta disponible")
            cursor = conn.cursor()
            cursor.execute(self.SQL_INSERT, (taller.getHorario(), taller.getMaquinaria(), taller.getConcesionario()))
    
            rows = cursor.rowcount

        except Error as e:
            print("Error al insertar taller:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows
