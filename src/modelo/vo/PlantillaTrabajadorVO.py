# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 12:27:47 2024

@author: ricar
"""

class PlantillaTrabajadorVO:
    def __init__(self, IDtrabajador=None, Contraseña=None, Nombre=None, Apellido1=None, Apellido2=None, Sueldo=None, Rol = None, Concesionario=None):
        self.IDtrabajador = IDtrabajador
        self.Contraseña = Contraseña
        self.Nombre = Nombre
        self.Apellido1 = Apellido1
        self.Apellido2 = Apellido2
        self.Sueldo = Sueldo
        self.rol = Rol
        self.Concesionario = Concesionario

    def getIDtrabajador(self):
        return self.IDtrabajador

    def setIDtrabajador(self, ID):
        self.IDtrabajador = ID

    def getContrasenia(self):
        return self.Contraseña

    def setContrasenia(self, contraseña):
        self.Contraseña = contraseña

    def getNombre(self):
        return self.Nombre

    def setNombre(self, nombre):
        self.Nombre = nombre

    def getApellido1(self):
        return self.Apellido1

    def setApellido1(self, apellido1):
        self.Apellido1 = apellido1

    def getApellido2(self):
        return self.Apellido2

    def setApellido2(self, apellido2):
        self.Apellido2 = apellido2

    def getSueldo(self):
        return self.Sueldo

    def setSueldo(self, sueldo):
        self.Sueldo = sueldo

    def getRol(self):
        return self.rol
    
    def setRol(self, r):
        self.rol = r

    def getConcesionario(self):
        return self.Concesionario

    def setConcesionario(self, concesionario):
        self.Concesionario = concesionario

    def toString(self):
        return f"IDtrabajador = {self.getIDtrabajador()}, Contrasenia = {self.getContrasenia()}, Nombre = {self.getNombre()}, Apellido1 = {self.getApellido1()}, Apellido2 = {self.getApellido2()}, Sueldo = {self.getSueldo()}, Rol = {self.getRol}, Concesionario = {self.getConcesionario()}"

    def __str__(self):
        return self.toString()