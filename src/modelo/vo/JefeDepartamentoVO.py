# -*- coding: utf-8 -*-
"""
Created on Thu May  2 21:04:18 2024

@author: Dell XPS 9510
"""

class JefeDepartamento:
    def __init__(self, IDjefeDepart=None, JefeZona=None):
        self.IDjefeDepart = IDjefeDepart
        self.JefeZona = JefeZona

    def getIDjefeDepart(self):
        return self.IDjefeDepart

    def setIDjefeDepart(self, ID):
        self.IDjefeDepart = ID

    def getJefeZona(self):
        return self.JefeZona

    def setJefeZona(self, ID):
        self.JefeZona = ID

    def toString(self):
        return f"IDjefeDepart = {self.getIDjefeDepart()}, JefeZona = {self.getJefeZona()}"

    def __str__(self):
        return self.toString()
