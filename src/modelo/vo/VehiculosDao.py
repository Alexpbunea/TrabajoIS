# -*- coding: utf-8 -*-
"""
Created on Fri May  3 13:37:27 2024

@author: Dell XPS 9510
"""

from jaydebeapi import Error
from typing import List
from src.modelo.vo.Vehiculo import Vehiculo
from src.modelo.conexion.conexionJava import Conexion
from src.modelo.dao.VehiculoInterface import VehiculoInterface

class VehiculoDao(VehiculoInterface, Conexion):
    # Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT IDvehiculo, Marca, Modelo, Anio, Combustible, Kilometros, Precio, Concesionario FROM Vehiculos"
    SQL_INSERT = "INSERT INTO Vehiculos(IDvehiculo, Marca, Modelo, Anio, Combustible, Kilometros, Precio, Concesionario) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

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
            # Crea un objeto para poder ejecutar consultas SQL sobre la conexión abierta
            cursor = conn.cursor()
            # Ejecuta la consulta SQL
            cursor.execute(self.SQL_SELECT)
            # Obtiene todas las filas resultantes de la consulta
            rows = cursor.fetchall()
            # Itera sobre todas las filas
            for row in rows:
                IDvehiculo, Marca, Modelo, Anio, Combustible, Kilometros, Precio, Concesionario = row
                # Crea un objeto Vehiculo para cada fila
                vehiculo = Vehiculo()
                vehiculo.setIDvehiculo(IDvehiculo)
                vehiculo.setMarca(Marca)
                vehiculo.setModelo(Modelo)
                vehiculo.setAnio(Anio)
                vehiculo.setCombustible(Combustible)
                vehiculo.setKilometros(Kilometros)
                vehiculo.setPrecio(Precio)
                vehiculo.setConcesionario(Concesionario)
                vehiculos.append(vehiculo)

        except Error as e:
            print("Error al seleccionar vehículos:", e)
        # Se ejecuta siempre
        finally:
            if cursor:
                # Cierra el cursor para liberar recursos
                cursor.close()

        conexion = self.closeConnection(conn)
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
            
            # Asegurarse de que esos cambios se hagan permanentes: conn.commit(). 
            # Si conn.autocommit = True no es necesario llamar explícitamente a conn.commit() después de cada inserción, 
            # ya que la base de datos confirma automáticamente cada instrucción.
            
            # Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount

        except Error as e:
            print("Error al insertar vehículo:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.closeConnection(conn)

        return rows
