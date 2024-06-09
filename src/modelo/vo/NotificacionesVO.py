# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 12:51:21 2024
@author: ricar
"""

class NotificacionVO:
    def __init__(self, ID = None, IDcliente=None,Tipo=None, Estado=None, Concesionario=None):
        self.ID = ID
        self.IDcliente =IDcliente
        self.Tipo = Tipo
        self.Estado = Estado
        self.Concesionario = Concesionario

    def getID(self):
        return self.ID
    
    def setID(self, id):
        self.ID = id
    
    def getIDcliente(self):
        return self.IDcliente
    
    def setIDcliente(self, ID):
        self.IDcliente=ID

    def getTipo(self):
        return self.Tipo

    def setTipo(self, tipo):
        self.Tipo = tipo

    def getEstado(self):
        return self.Estado

    def setEstado(self, estado):
        self.Estado = estado

    def getConcesionario(self):
        return self.Concesionario

    def setConcesionario(self, concesionario):
        self.Concesionario = concesionario

    def __str__(self):
        return f"IDvehiculo: {self.ID}, IDcliente: {self.IDcliente}, Tipo: {self.Tipo}, Estado: {self.Estado}, Concesionario: {self.Concesionario}"
