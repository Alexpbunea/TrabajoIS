# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 12:51:21 2024

@author: ricar
"""

class AlmacenVO:
    def __init__(self, capacidad=None, piezas=None, porcentajeOcupado = None, concesionario = None):
        self.capacidad = capacidad
        self.piezas = piezas
        self.porcentajeOcupado = porcentajeOcupado
        self.concesionario = concesionario
        
    def getCapacidad(self):
        return self.capacidad
    def setCapacidad(self, capacidad):
        self.capacidad = capacidad
    
    def getPiezas(self):
        return self.piezas
    def setPiezas(self, piezas):
        self.piezas = piezas

    def getPorcentajeOcupado(self):
        return self.porcentajeOcupado
    
    def setPorcentajeOcupado(self, ocupado):
        self.porcentajeOcupado = ocupado
    
    def getConcesionario(self):
        return self.concesionario
    
    def setConcesionario(self, con):
        self.concesionario = con
        
    def toString(self):
        return f"Capacidad = {self.getCapacidad()}, piezas={self.getPiezas()}, porcentajeOcupado={self.getPorcentajeOcupado()}"
    
    def __str__(self):
        return self.toString()