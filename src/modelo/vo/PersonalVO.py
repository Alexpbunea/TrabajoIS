# -*- coding: utf-8 -*-
"""
Created on Thu May  2 21:05:07 2024

@author: Dell XPS 9510
"""

class Personal:
    def __init__(self, IDpersonal=None, JefeDepartamento=None):
        self.IDpersonal = IDpersonal
        self.JefeDepartamento = JefeDepartamento

    def getIDpersonal(self):
        return self.IDpersonal

    def setIDpersonal(self, ID):
        self.IDpersonal = ID

    def getJefeDepartamento(self):
        return self.JefeDepartamento

    def setJefeDepartamento(self, ID):
        self.JefeDepartamento = ID

    def toString(self):
        return f"IDpersonal = {self.getIDpersonal()}, JefeDepartamento = {self.getJefeDepartamento()}"

    def __str__(self):
        return self.toString()
