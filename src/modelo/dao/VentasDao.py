# -*- coding: utf-8 -*-
"""
Created on Fri May  3 13:39:09 2024

@author: Dell XPS 9510
"""

from jaydebeapi import Error
from typing import List
from src.modelo.vo.Venta import Venta
from src.modelo.conexion.conexionJava import Conexion
from src.modelo.dao.VentaInterface import VentaInterface

class VentaDao(VentaInterface, Conexion):
    # Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT IDventa, FechaVenta, IDvehiculo, IDcliente, Concesionario FROM Ventas"
    SQL_INSERT = "INSERT INTO Ventas(IDventa, FechaVenta, IDvehiculo, IDcliente, Concesionario) VALUES (?, ?, ?, ?, ?)"

    def getVentas(self) -> List[Venta]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        ventas = []

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
                IDventa, FechaVenta, IDvehiculo, IDcliente, Concesionario = row
                # Crea un objeto Venta para cada fila
                venta = Venta()
                venta.setIDventa(IDventa)
                venta.setFechaVenta(FechaVenta)
                venta.setIDvehiculo(IDvehiculo)
                venta.setIDcliente(IDcliente)
                venta.setConcesionario(Concesionario)
                ventas.append(venta)

        except Error as e:
            print("Error al seleccionar ventas:", e)
        # Se ejecuta siempre
        finally:
            if cursor:
                # Cierra el cursor para liberar recursos
                cursor.close()

        conexion = self.closeConnection(conn)
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
                print("La base de datos no esta disponible")
            cursor = conn.cursor()
            cursor.execute(self.SQL_INSERT, (venta.getIDventa(), venta.getFechaVenta(), venta.getIDvehiculo(), venta.getIDcliente(), venta.getConcesionario()))
            
            rows = cursor.rowcount

        except Error as e:
            print("Error al insertar venta:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows
