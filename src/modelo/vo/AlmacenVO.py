# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 12:51:21 2024

@author: ricar
"""

class AlmacenVO:
    def __init__(self, capacidad=None, piezas=None):
        self.capacidad = capacidad
        self.piezas = piezas
        
    def getCapacidad(self):
        return self.capacidad
    def setCapacidad(self, capacidad):
        self.capacidad = capacidad
    
    def getNombre(self):
        return self.piezas
    def setNombre(self, piezas):
        self.piezas = piezas
        
    def toString(self):
        return "AlmacenVO("+"Capacidad="+str(self.capacidad)+", piezas="+str(self.piezas)+")"
    def __str__(self):
        return self.toString()