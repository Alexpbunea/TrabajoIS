# -*- coding: utf-8 -*-
"""
Created on Fri May  3 13:39:09 2024

@author: Dell XPS 9510
"""

from jaydebeapi import Error
from typing import List
from src.modelo.vo.VentasVO import Venta
from src.modelo.conexion.conexionJava import Conexion
from src.modelo.dao.VentaInterface import VentaInterface

class VentaDao(VentaInterface, Conexion):
    # Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT IDventa, FechaVenta, IDvehiculo, Repara, IDcliente, Piezas, Cantidad, Concesionario FROM ventas"
    SQL_INSERT = "INSERT INTO ventas(FechaVenta, IDvehiculo, Repara, IDcliente, Piezas, Cantidad, Concesionario) VALUES (?, ?, ?, ?, ?, ?, ?)"
    SQL_UPDATE = "UPDATE ventas SET FechaVenta = ?, IDvehiculo = ?, Repara = ?, IDcliente = ?, Piezas = ?, Cantidad = ?, Concesionario = ? WHERE IDventa = ?"
    SQL_DELETE = "DELETE FROM ventas WHERE IDventa = ?"

    def getVentas(self) -> List[Venta]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        ventas = []

        try:
            if conexion:
                conn = conexion             
            else:
                print("La base de datos no está disponible")            
            # Crea un objeto para poder ejecutar consultas SQL sobre la conexión abierta
            cursor = conn.cursor()
            # Ejecuta la consulta SQL
            cursor.execute(self.SQL_SELECT)
            # Obtiene todas las filas resultantes de la consulta
            rows = cursor.fetchall()
            # Itera sobre todas las filas
            for row in rows:
                IDventa, FechaVenta, IDvehiculo, Repara, IDcliente, Piezas, Cantidad, Concesionario = row
                # Crea un objeto Venta para cada fila
                venta = Venta()
                venta.setIDventa(IDventa)
                venta.setFechaVenta(FechaVenta)
                venta.setIDvehiculo(IDvehiculo)
                venta.setRepara(Repara)
                venta.setIDcliente(IDcliente)
                venta.setPiezas(Piezas)
                venta.setCantidad(Cantidad)
                venta.setConcesionario(Concesionario)
                ventas.append(venta)

        except Error as e:
            print("Error al seleccionar ventas:", e)
        # Se ejecuta siempre
        finally:
            if cursor:
                # Cierra el cursor para liberar recursos
                cursor.close()

        conexion = self.close(conn)
        return ventas
    
    def insertVenta(self, venta: Venta) -> int:
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
            cursor.execute(self.SQL_INSERT, (venta.getFechaVenta(), venta.getIDvehiculo(), venta.getRepara(), venta.getIDcliente(), venta.getPiezas(), venta.getCantidad(), venta.getConcesionario()))
            
            rows = cursor.rowcount

        except Error as e:
            print("Error al insertar venta:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.close(conn)

        return rows
    
    def updateVenta(self, venta: Venta) -> int:
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
            cursor.execute(self.SQL_UPDATE, (venta.getFechaVenta(), venta.getIDvehiculo(), venta.getRepara(), venta.getIDcliente(), venta.getPiezas(), venta.getCantidad(), venta.getConcesionario(), venta.getIDventa()))
            
            rows = cursor.rowcount

        except Error as e:
            print("Error al actualizar venta:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.close(conn)

        return rows
    
    def deleteVenta(self, id_venta: int) -> int:
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
            cursor.execute(self.SQL_DELETE, (id_venta,))
            
            rows = cursor.rowcount

        except Error as e:
            print("Error al eliminar venta:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.close(conn)

        return rows
