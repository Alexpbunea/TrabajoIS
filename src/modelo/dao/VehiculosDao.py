# -*- coding: utf-8 -*-
"""
Created on Fri May  3 13:37:27 2024

@author: Dell XPS 9510
"""

from jaydebeapi import Error
from typing import List
from src.modelo.vo.VehiculosVO import Vehiculo
from src.modelo.conexion.conexionJava import Conexion
from src.modelo.dao.VehiculoInterface import VehiculoInterface

class VehiculoDao(VehiculoInterface, Conexion):
    # Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT IDvehiculo, Marca, Modelo, Año, Combustible, Kilometros, Precio, Concesionario FROM vehiculos"
    SQL_INSERT = "INSERT INTO vehiculos(IDvehiculo, Marca, Modelo, Año, Combustible, Kilometros, Precio, Concesionario) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    SQL_UPDATE = "UPDATE vehiculos SET Marca=?, Modelo=?, Año=?, Combustible=?, Kilometros=?, Precio=?, Concesionario=? WHERE IDvehiculo=?"
    SQL_DELETE = "DELETE FROM vehiculos WHERE IDvehiculo=?"

    def getVehiculos(self) -> List[Vehiculo]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        vehiculos = []

        try:
            if conexion:
                conn = conexion             
            else:
                print("La base de datos no está disponible")            
            cursor = conn.cursor()
            cursor.execute(self.SQL_SELECT)
            rows = cursor.fetchall()
            for row in rows:
                IDvehiculo, Marca, Modelo, Año, Combustible, Kilometros, Precio, Concesionario = row
                vehiculo = Vehiculo()
                vehiculo.setIDvehiculo(IDvehiculo)
                vehiculo.setMarca(Marca)
                vehiculo.setModelo(Modelo)
                vehiculo.setAnio(Año)
                vehiculo.setCombustible(Combustible)
                vehiculo.setKilometros(Kilometros)
                vehiculo.setPrecio(Precio)
                vehiculo.setConcesionario(Concesionario)
                vehiculos.append(vehiculo)

        except Error as e:
            print("Error al seleccionar vehículos:", e)
        finally:
            if cursor:
                cursor.close()

        conexion = self.close(conn)
        return vehiculos
    

    def insertVehiculo(self, vehiculo: Vehiculo) -> int:
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
            cursor.execute(self.SQL_INSERT, (vehiculo.getIDvehiculo(), vehiculo.getMarca(), vehiculo.getModelo(), vehiculo.getAnio(), vehiculo.getCombustible(), vehiculo.getKilometros(), vehiculo.getPrecio(), vehiculo.getConcesionario()))
            rows = cursor.rowcount

        except Error as e:
            print("Error al insertar vehículo:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.close(conn)
        return rows

    def modificarVehiculo(self, vehiculo: Vehiculo) -> int:
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
            cursor.execute(self.SQL_UPDATE, (vehiculo.getMarca(), vehiculo.getModelo(), vehiculo.getAnio(), vehiculo.getCombustible(), vehiculo.getKilometros(), vehiculo.getPrecio(), vehiculo.getConcesionario(), vehiculo.getIDvehiculo()))
            rows = cursor.rowcount

        except Error as e:
            print("Error al modificar vehículo:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.close(conn)
        return rows

    def deteteVehiculo(self, IDvehiculo: str) -> int:
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
            cursor.execute(self.SQL_DELETE, (IDvehiculo,))
            rows = cursor.rowcount

        except Error as e:
            print("Error al eliminar vehículo:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.close(conn)
        return rows
