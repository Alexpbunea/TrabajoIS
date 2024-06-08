# -*- coding: utf-8 -*-
"""
Created on Thu May  2 21:06:23 2024

@author: Dell XPS 9510
"""

class Pago:
    def __init__(self, IDpago=None, Precio=None, IDventa=None, Concesionario=None):
        self.IDpago = IDpago
        self.Precio = Precio
        self.IDventa = IDventa
        self.Concesionario = Concesionario

    def getIDpago(self):
        return self.IDpago

    def setIDpago(self, ID):
        self.IDpago = ID

    def getPrecio(self):
        return self.Precio

    def setPrecio(self, precio):
        self.Precio = precio

    def getIDventa(self):
        return self.IDventa

    def setIDventa(self, ID):
        self.IDventa = ID

    def getConcesionario(self):
        return self.Concesionario

    def setConcesionario(self, nombre):
        self.Concesionario = nombre

    def toString(self):
        return f"IDpago = {self.getIDpago()}, Precio = {self.getPrecio()}, IDventa = {self.getIDventa()}, Concesionario = {self.getConcesionario()}"

    def __str__(self):
        return self.toString()
