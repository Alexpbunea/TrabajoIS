# -*- coding: utf-8 -*-
"""
Created on Fri May  3 13:19:20 2024

@author: Dell XPS 9510
"""

from jaydebeapi import Error
from typing import List
from src.modelo.vo.NotificacionesVO import NotificacionVO as Notificacion
from src.modelo.conexion.conexionJava import Conexion
from src.modelo.dao.NotificacionInterfaze import NotificacionInterface

class NotificacionDao(NotificacionInterface, Conexion):
    SQL_SELECT = "SELECT IDnotificacion, IDcliente, Tipo, Estado, Concesionario FROM notificaciones"
    SQL_INSERT = "INSERT INTO notificaciones (IDnotificacion, IDcliente, Tipo, Estado, Concesionario) VALUES (?, ?, ?, ?, ?)"
    SQL_UPDATE = "UPDATE notificaciones SET IDcliente=?, Tipo=?, Estado=?, Concesionario=? WHERE IDnotificacion=?"
    SQL_DELETE = "DELETE FROM notificaciones WHERE IDnotificacion=?"

    def getNotificaciones(self) -> List[Notificacion]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        notificaciones = []

        try:
            if conexion:
                conn = conexion             
            else:
                print("La base de datos no está disponible")            
            cursor = conn.cursor()
            cursor.execute(self.SQL_SELECT)
            rows = cursor.fetchall()
            for row in rows:
                IDnotificacion, IDcliente, Tipo, Estado, Concesionario = row
                notificacion = Notificacion(IDnotificacion, IDcliente, Tipo, Estado, Concesionario)
                notificaciones.append(notificacion)

        except Error as e:
            print("Error al seleccionar notificaciones:", e)
        finally:
            if cursor:
                cursor.close()

        conexion = self.close(conn)
        return notificaciones

    def insertNotificacion(self, notificacion: Notificacion) -> int:
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
            cursor.execute(self.SQL_INSERT, (notificacion.getID(),notificacion.getIDcliente() ,notificacion.getTipo(), notificacion.getEstado(), notificacion.getConcesionario()))
            rows = cursor.rowcount

        except Error as e:
            print("Error al insertar notificación:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.close(conn)
        return rows

    def updateNotificacion(self, notificacion: Notificacion) -> int:
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
            cursor.execute(self.SQL_UPDATE, (notificacion.getIDcliente(), notificacion.getTipo(), notificacion.getEstado(), notificacion.getConcesionario(), notificacion.getID()))
            rows = cursor.rowcount

        except Error as e:
            print("Error al actualizar notificación:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.close(conn)
        return rows

    def deleteNotificacion(self, IDnotificacion: int) -> int:
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
            cursor.execute(self.SQL_DELETE, (IDnotificacion,))
            rows = cursor.rowcount

        except Error as e:
            print("Error al eliminar notificación:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.close(conn)
        return rows
