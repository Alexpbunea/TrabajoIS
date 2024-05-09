# -*- coding: utf-8 -*-
"""
Created on Thu May  2 21:01:48 2024

@author: Dell XPS 9510
"""

class Venta:
    def __init__(self, IDventa=None, FechaVenta=None, IDvehiculo=None, IDcliente=None, Concesionario=None):
        self.IDventa = IDventa
        self.FechaVenta = FechaVenta
        self.IDvehiculo = IDvehiculo
        self.IDcliente = IDcliente
        self.Concesionario = Concesionario

    def getIDventa(self):
        return self.IDventa

    def setIDventa(self, ID):
        self.IDventa = ID

    def getFechaVenta(self):
        return self.FechaVenta

    def setFechaVenta(self, fecha):
        self.FechaVenta = fecha

    def getIDvehiculo(self):
        return self.IDvehiculo

    def setIDvehiculo(self, ID):
        self.IDvehiculo = ID

    def getIDcliente(self):
        return self.IDcliente

    def setIDcliente(self, ID):
        self.IDcliente = ID

    def getConcesionario(self):
        return self.Concesionario

    def setConcesionario(self, nombre):
        self.Concesionario = nombre

    def toString(self):
        return f"IDventa = {self.getIDventa()}, FechaVenta = {self.getFechaVenta()}, IDvehiculo = {self.getIDvehiculo()}, IDcliente = {self.getIDcliente()}, Concesionario = {self.getConcesionario()}"

    def __str__(self):
        return self.toString()
