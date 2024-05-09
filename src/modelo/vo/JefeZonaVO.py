# -*- coding: utf-8 -*-
"""
Created on Thu May  2 21:04:02 2024

@author: Dell XPS 9510
"""

class JefeZona:
    def __init__(self, IDjefeZona=None):
        self.IDjefeZona = IDjefeZona

    def getIDjefeZona(self):
        return self.IDjefeZona

    def setIDjefeZona(self, ID):
        self.IDjefeZona = ID

    def toString(self):
        return f"IDjefeZona = {self.getIDjefeZona()}"

    def __str__(self):
        return self.toString()
