# -*- coding: utf-8 -*-
"""
Created on Fri May  3 13:26:32 2024

@author: Dell XPS 9510
"""

from jaydebeapi import Error
from typing import List
from src.modelo.vo.PagoVO import Pago
from src.modelo.conexion.conexionJava import Conexion
from src.modelo.dao.PagoInterface import PagoInterface

class PagoDao(PagoInterface, Conexion):
    # Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT IDpago, Precio, IDventa, Concesionario FROM pago"
    SQL_INSERT = "INSERT INTO pago(Precio, IDventa, Concesionario) VALUES (?, ?, ?)"
    SQL_UPDATE = "UPDATE pago SET Precio = ?, IDventa = ?, Concesionario = ? WHERE IDpago = ?"
    SQL_DELETE = "DELETE FROM pago WHERE IDpago = ?"

    def getPagos(self) -> List[Pago]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        pagos = []

        try:
            if conexion:
                conn = conexion             
            else:
                print("La base de datos no está disponible")            
            cursor = conn.cursor()
            cursor.execute(self.SQL_SELECT)
            rows = cursor.fetchall()
            for row in rows:
                IDpago, Precio, IDventa, Concesionario = row
                pago = Pago()
                pago.setIDpago(IDpago)
                pago.setPrecio(Precio)
                pago.setIDventa(IDventa)
                pago.setConcesionario(Concesionario)
                pagos.append(pago)

        except Error as e:
            print("Error al seleccionar pagos:", e)
        finally:
            if cursor:
                cursor.close()
            self.close(conn)

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
                print("La base de datos no está disponible")
            cursor = conn.cursor()
            cursor.execute(self.SQL_INSERT, (pago.getPrecio(), pago.getIDventa(), pago.getConcesionario()))
            rows = cursor.rowcount

        except Error as e:
            print("Error al insertar pago:", e)
        finally:
            if cursor:
                cursor.close()
            self.close(conn)

        return rows

    def updatePago(self, pago: Pago) -> int:
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
            cursor.execute(self.SQL_UPDATE, (pago.getPrecio(), pago.getIDventa(), pago.getConcesionario(), pago.getIDpago()))
            rows = cursor.rowcount

        except Error as e:
            print("Error al actualizar pago:", e)
        finally:
            if cursor:
                cursor.close()
            self.close(conn)

        return rows

    def deletePago(self, IDpago: int) -> int:
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
            cursor.execute(self.SQL_DELETE, (IDpago,))
            rows = cursor.rowcount

        except Error as e:
            print("Error al eliminar pago:", e)
        finally:
            if cursor:
                cursor.close()
            self.close(conn)

        return rows