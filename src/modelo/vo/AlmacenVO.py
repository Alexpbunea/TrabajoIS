# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 12:51:21 2024

@author: ricar
"""

class AlmacenVO:
    def __init__(self, Pieza=None, Cantidad=None, PrecioPieza=None, Concesionario=None):
        self.Pieza = Pieza
        self.Cantidad = Cantidad
        self.PrecioPieza = PrecioPieza
        self.Concesionario = Concesionario

    def getPieza(self):
        return self.Pieza

    def setPieza(self, pieza):
        self.Pieza = pieza

    def getCantidad(self):
        return self.Cantidad

    def setCantidad(self, cantidad):
        self.Cantidad = cantidad

    def getPrecioPieza(self):
        return self.PrecioPieza

    def setPrecioPieza(self, precio):
        self.PrecioPieza = precio

    def getConcesionario(self):
        return self.Concesionario

    def setConcesionario(self, concesionario):
        self.Concesionario = concesionario

    def __str__(self):
        return f"Pieza: {self.Pieza}, Cantidad: {self.Cantidad}, PrecioPieza: {self.PrecioPieza}, Concesionario: {self.Concesionario}"