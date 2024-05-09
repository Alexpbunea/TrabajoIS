# -*- coding: utf-8 -*-
"""
Created on Thu May  2 21:02:38 2024

@author: Dell XPS 9510
"""

class Taller:
    def __init__(self, horario=None, Maquinaria=None, Concesionario=None):
        self.horario = horario
        self.Maquinaria = Maquinaria
        self.Concesionario = Concesionario

    def getHorario(self):
        return self.horario

    def setHorario(self, horario):
        self.horario = horario

    def getMaquinaria(self):
        return self.Maquinaria

    def setMaquinaria(self, maquinaria):
        self.Maquinaria = maquinaria

    def getConcesionario(self):
        return self.Concesionario

    def setConcesionario(self, concesionario):
        self.Concesionario = concesionario

    def toString(self):
        return f"Horario = {self.getHorario()}, Maquinaria = {self.getMaquinaria()}, Concesionario = {self.getConcesionario()}"

    def __str__(self):
        return self.toString()
