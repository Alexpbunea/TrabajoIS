# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 13:05:03 2024

@author: Dell XPS 9510
"""

from jaydebeapi import Error
from typing import List
from src.modelo.vo.ClienteVO import Cliente
from src.modelo.conexion.conexionJava import Conexion
from src.modelo.dao.ClienteInterface import ClienteInterface

class ClienteDao(ClienteInterface, Conexion):
    # Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT IDcliente, Contrasenia, Nombre, Apellido1, Apellido2, Direccion, Email, Concesionario FROM Clientes"
    SQL_INSERT = "INSERT INTO Clientes(IDcliente, Contrasenia, Nombre, Apellido1, Apellido2, Direccion, Email, Concesionario) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

    def getClientes(self) -> List[Cliente]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        clientes = []

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
                IDcliente, Contrasenia, Nombre, Apellido1, Apellido2, Direccion, Email, Concesionario = row
                # Crea un objeto Cliente para cada fila
                cliente = Cliente()
                cliente.setIDcliente(IDcliente)
                cliente.setContrasenia(Contrasenia)
                cliente.setNombre(Nombre)
                cliente.setApellido1(Apellido1)
                cliente.setApellido2(Apellido2)
                cliente.setDireccion(Direccion)
                cliente.setEmail(Email)
                cliente.setConcesionario(Concesionario)
                clientes.append(cliente)

        except Error as e:
            print("Error al seleccionar clientes:", e)
        # Se ejecuta siempre
        finally:
            if cursor:
                # Cierra el cursor para liberar recursos
                cursor.close()

        conexion = self.closeConnection(conn)
        return clientes
    

    def insertCliente(self, cliente: Cliente) -> int:
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
            cursor.execute(self.SQL_INSERT, (cliente.getIDcliente(), cliente.getContrasenia(), cliente.getNombre(), cliente.getApellido1(), cliente.getApellido2(), cliente.getDireccion(), cliente.getEmail(), cliente.getConcesionario()))
            
            rows = cursor.rowcount

        except Error as e:
            print("Error al insertar cliente:", e)

        finally:
            if cursor:
                cursor.close()

        self.close(conn)

        return rows

            
        
    