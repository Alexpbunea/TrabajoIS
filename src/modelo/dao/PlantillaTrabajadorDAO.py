from jaydebeapi import Error
from typing import List
from src.modelo.vo.PlantillaTrabajadorVO import PlantillaTrabajadorVO
from src.modelo.conexion.conexionJava import Conexion
from src.modelo.dao.TrabajadorInterface import TrabajadorInterface

class TrabajadorDao(TrabajadorInterface, Conexion):
    # Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT IDtrabajador, Contrasenia, Nombre, Apellido1, Apellido2, Sueldo, Rol, Concesionario FROM plantillatrabajadores"
    SQL_INSERT = "INSERT INTO plantillatrabajadores(IDtrabajador, Contrasenia, Nombre, Apellido1, Apellido2, Sueldo, Rol, Concesionario) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    SQL_DELETE = "DELETE FROM plantillatrabajadores WHERE IDtrabajador = ?"
    SQL_UPDATE = "UPDATE plantillatrabajadores SET Contrasenia = ?, Nombre = ?, Apellido1 = ?, Apellido2 = ?, Sueldo = ?, Rol = ?, Concesionario = ? WHERE IDtrabajador = ?"

    def getTrabajadores(self) -> List[PlantillaTrabajadorVO]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        trabajadores = []

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
                IDtrabajador, Contrasenia, Nombre, Apellido1, Apellido2, Sueldo, Rol, Concesionario = row
                # Crea un objeto PlantillaTrabajadorVO para cada fila
                trabajador = PlantillaTrabajadorVO()
                trabajador.setIDtrabajador(IDtrabajador)
                trabajador.setContrasenia(Contrasenia)
                trabajador.setNombre(Nombre)
                trabajador.setApellido1(Apellido1)
                trabajador.setApellido2(Apellido2)
                trabajador.setSueldo(Sueldo)
                trabajador.setRol(Rol)
                trabajador.setConcesionario(Concesionario)
                trabajadores.append(trabajador)

        except Error as e:
            print("Error al seleccionar trabajadores:", e)
        # Se ejecuta siempre
        finally:
            if cursor:
                # Cierra el cursor para liberar recursos
                cursor.close()

        conexion = self.close(conn)
        return trabajadores
    

    def insertTrabajador(self, trabajador: PlantillaTrabajadorVO) -> int:
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
            cursor.execute(self.SQL_INSERT, (trabajador.getIDtrabajador(), trabajador.getContrasenia(), trabajador.getNombre(), trabajador.getApellido1(), trabajador.getApellido2(), trabajador.getSueldo(), trabajador.getRol(), trabajador.getConcesionario()))
            
            # Asegurarse de que esos cambios se hagan permanentes: conn.commit(). 
            # Si conn.autocommit = True no es necesario llamar explicitamente a conn.commit() despues de cada insercion, 
            # ya que la base de datos confirma automaticamente cada instruccion.
            
            # Devuelve 1 si la insercion fue exitosa
            rows = cursor.rowcount

        except Error as e:
            print("Error al insertar trabajador:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.close(conn)

        return rows

    def deleteTrabajador(self, IDtrabajador: str) -> int:
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
            cursor.execute(self.SQL_DELETE, (IDtrabajador,))
            rows = cursor.rowcount

        except Error as e:
            print("Error al eliminar trabajador:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.close(conn)
        return rows

    def updateTrabajador(self, trabajador: PlantillaTrabajadorVO) -> int:
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
            cursor.execute(self.SQL_UPDATE, (trabajador.getContrasenia(), trabajador.getNombre(), trabajador.getApellido1(), trabajador.getApellido2(), trabajador.getSueldo(), trabajador.getRol(), trabajador.getConcesionario(), trabajador.getIDtrabajador()))
            rows = cursor.rowcount

        except Error as e:
            print("Error al actualizar trabajador:", e)

        finally:
            if cursor:
                cursor.close()

        conexion = self.close(conn)
        return rows