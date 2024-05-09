# -*- coding: utf-8 -*-
"""
Created on Fri May  3 13:22:26 2024

@author: Dell XPS 9510
"""

from jaydebeapi import Error
from typing import List
from src.modelo.vo.JefeDepartamento import JefeDepartamento
from src.modelo.conexion.conexionJava import Conexion
from src.modelo.dao.JefeDepartamentoInterface import JefeDepartamentoInterface

class JefeDepartamentoDao(JefeDepartamentoInterface, Conexion):
    # Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT IDjefeDepart, JefeZona FROM JefesDepartamento"
    SQL_INSERT = "INSERT INTO JefesDepartamento(IDjefeDepart, JefeZona) VALUES (?, ?)"

    def getJefesDepartamento(self) -> List[JefeDepartamento]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        jefes_departamento = []

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
                IDjefeDepart, JefeZona = row
                # Crea un objeto JefeDepartamento para cada fila
                jefe_departamento = JefeDepartamento()
                jefe_departamento.setIDjefeDepart(IDjefeDepart)
                jefe_departamento.setJefeZona(JefeZona)
                jefes_departamento.append(jefe_departamento)

        except Error as e:
            print("Error al seleccionar jefes de departamento:", e)
        # Se ejecuta siempre
        finally:
            if cursor:
                # Cierra el cursor para liberar recursos
                cursor.close()

        conexion = self.closeConnection(conn)
        return jefes_departamento
    

    def insertJefeDepartamento(self, jefe_departamento: JefeDepartamento) -> int:
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
            cursor.execute(self.SQL_INSERT, (jefe_departamento.getIDjefeDepart(), jefe_departamento.getJefeZona()))
            
            rows = cursor.rowcount

        except Error as e:
            print("Error al insertar jefe de departamento:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows
