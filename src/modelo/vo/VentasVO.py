# -*- coding: utf-8 -*-
"""
Created on Thu May  2 21:01:48 2024
@author: Dell XPS 9510
"""

class Venta:
    def __init__(self, IDventa=None, FechaVenta=None, IDvehiculo=None, Repara=None, IDcliente=None, Piezas=None, Cantidad=None, Concesionario=None):
        self.IDventa = IDventa
        self.FechaVenta = FechaVenta
        self.IDvehiculo = IDvehiculo
        self.Repara = Repara
        self.IDcliente = IDcliente
        self.Piezas = Piezas
        self.Cantidad = Cantidad
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

    def getRepara(self):
        return self.Repara

    def setRepara(self, rep):
        self.Repara = rep

    def getIDcliente(self):
        return self.IDcliente

    def setIDcliente(self, ID):
        self.IDcliente = ID

    def getPiezas(self):
        return self.Piezas
    
    def setPiezas(self, piezas):
        self.Piezas = piezas

    def getCantidad(self):
        return self.Cantidad
    
    def setCantidad(self, cantidad):
        self.Cantidad = cantidad

    def getConcesionario(self):
        return self.Concesionario

    def setConcesionario(self, nombre):
        self.Concesionario = nombre

    def toString(self):
        return f"IDventa = {self.getIDventa()}, FechaVenta = {self.getFechaVenta()}, IDvehiculo = {self.getIDvehiculo()}, Repara = {self.getRepara()}, IDcliente = {self.getIDcliente()}, Piezas = {self.getPiezas()}, Cantidad = {self.getCantidad()}, Concesionario = {self.getConcesionario()}"

    def __str__(self):
        return self.toString()
