# -*- coding: utf-8 -*-
"""
Created on Thu May  2 21:06:23 2024

@author: Dell XPS 9510
"""

class Pago:
    def __init__(self, IDpago=None, FacturaPDF=None, Concesionario=None):
        self.IDpago = IDpago
        self.FacturaPDF = FacturaPDF
        self.concesionario = Concesionario

    def getIDpago(self):
        return self.IDpago

    def setIDpago(self, ID):
        self.IDpago = ID

    def getFacturaPDF(self):
        return self.FacturaPDF

    def setFacturaPDF(self, factura):
        self.FacturaPDF = factura
    
    def getConcesionario(self):
        return self.concesionario
    
    def setConcesionario(self, con):
        self.concesionario = con

    def toString(self):
        return f"IDpago = {self.getIDpago()}, FacturaPDF = {self.getFacturaPDF()}, Concesionario = {self.getConcesionario}"

    def __str__(self):
        return self.toString()
