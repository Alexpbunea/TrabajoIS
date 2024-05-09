# -*- coding: utf-8 -*-
"""
Created on Fri May  3 13:26:32 2024

@author: Dell XPS 9510
"""

from jaydebeapi import Error
from typing import List
from src.modelo.vo.Pago import Pago
from src.modelo.conexion.conexionJava import Conexion
from src.modelo.dao.PagoInterface import PagoInterface

class PagoDao(PagoInterface, Conexion):
    # Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT IDpago, FacturaPDF FROM Pagos"
    SQL_INSERT = "INSERT INTO Pagos(IDpago, FacturaPDF) VALUES (?, ?)"

    def getPagos(self) -> List[Pago]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        pagos = []

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
                IDpago, FacturaPDF = row
                # Crea un objeto Pago para cada fila
                pago = Pago()
                pago.setIDpago(IDpago)
                pago.setFacturaPDF(FacturaPDF)
                pagos.append(pago)

        except Error as e:
            print("Error al seleccionar pagos:", e)
        # Se ejecuta siempre
        finally:
            if cursor:
                # Cierra el cursor para liberar recursos
                cursor.close()

        conexion = self.closeConnection(conn)
        return pagos
    

    def insertPago(self, pago: Pago) -> int:
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
            cursor.execute(self.SQL_INSERT, (pago.getIDpago(), pago.getFacturaPDF()))
            
            rows = cursor.rowcount

        except Error as e:
            print("Error al insertar pago:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows
