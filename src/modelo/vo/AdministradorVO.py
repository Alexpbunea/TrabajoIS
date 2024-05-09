# -*- coding: utf-8 -*-
"""
Created on Thu May  2 21:03:22 2024

@author: Dell XPS 9510
"""

class Administrador:
    def __init__(self, IDadmin=None):
        self.IDadmin = IDadmin

    def getIDadmin(self):
        return self.IDadmin

    def setIDadmin(self, ID):
        self.IDadmin = ID

    def toString(self):
        return f"IDadmin = {self.getIDadmin()}"

    def __str__(self):
        return self.toString()
