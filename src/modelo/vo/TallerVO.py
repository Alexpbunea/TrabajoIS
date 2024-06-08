# -*- coding: utf-8 -*-
"""
Created on Thu May  2 21:02:38 2024

@author: Dell XPS 9510
"""

class Taller:
    def __init__(self, IDmaquinaria=None, Maquinaria=None, Cantidad=None, Concesionario=None):
        self.IDmaquinaria = IDmaquinaria
        self.Maquinaria = Maquinaria
        self.Cantidad = Cantidad
        self.Concesionario = Concesionario

    def getIDmaquinaria(self):
        return self.IDmaquinaria

    def setIDmaquinaria(self, id_maquinaria):
        self.IDmaquinaria = id_maquinaria

    def getMaquinaria(self):
        return self.Maquinaria

    def setMaquinaria(self, maquinaria):
        self.Maquinaria = maquinaria

    def getCantidad(self):
        return self.Cantidad

    def setCantidad(self, cantidad):
        self.Cantidad = cantidad

    def getConcesionario(self):
        return self.Concesionario

    def setConcesionario(self, concesionario):
        self.Concesionario = concesionario

    def __str__(self):
        return f"IDmaquinaria: {self.IDmaquinaria}, Maquinaria: {self.Maquinaria}, Cantidad: {self.Cantidad}, Concesionario: {self.Concesionario}"