# -*- coding: utf-8 -*-
"""
Created on Fri May  3 13:34:50 2024

@author: Dell XPS 9510
"""

from jaydebeapi import Error
from typing import List
from src.modelo.vo.PersonalVO import Personal
from src.modelo.conexion.conexionJava import Conexion
from src.modelo.dao.PersonalInterface import PersonalInterface

class PersonalDao(PersonalInterface, Conexion):
    # Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT IDpersonal, JefeDepartamento FROM Personal"
    SQL_INSERT = "INSERT INTO Personal(IDpersonal, JefeDepartamento) VALUES (?, ?)"

    def getPersonal(self) -> List[Personal]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        personal = []

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
                IDpersonal, JefeDepartamento = row
                # Crea un objeto Personal para cada fila
                person = Personal()
                person.setIDpersonal(IDpersonal)
                person.setJefeDepartamento(JefeDepartamento)
                personal.append(person)

        except Error as e:
            print("Error al seleccionar personal:", e)
        # Se ejecuta siempre
        finally:
            if cursor:
                # Cierra el cursor para liberar recursos
                cursor.close()

        conexion = self.closeConnection(conn)
        return personal
    

    def insertPersonal(self, person: Personal) -> int:
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
            cursor.execute(self.SQL_INSERT, (person.getIDpersonal(), person.getJefeDepartamento()))
        
            rows = cursor.rowcount

        except Error as e:
            print("Error al insertar personal:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows
