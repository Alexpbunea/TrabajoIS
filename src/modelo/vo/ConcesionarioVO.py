# -*- coding: utf-8 -*-
"""
Created on Thu May  2 21:07:59 2024

@author: Dell XPS 9510
"""

class Concesionario:
    def __init__(self, Nombre=None, Direccion=None, Ciudad=None, FechaInauguracion=None):
        self.Nombre = Nombre
        self.Direccion = Direccion
        self.Ciudad = Ciudad
        self.FechaInauguracion = FechaInauguracion

    def getNombre(self):
        return self.Nombre

    def setNombre(self, nombre):
        self.Nombre = nombre

    def getDireccion(self):
        return self.Direccion

    def setDireccion(self, direccion):
        self.Direccion = direccion

    def getCiudad(self):
        return self.Ciudad

    def setCiudad(self, ciudad):
        self.Ciudad = ciudad

    def getFechaInauguracion(self):
        return self.FechaInauguracion

    def setFechaInauguracion(self, fecha):
        self.FechaInauguracion = fecha

    def toString(self):
        return f"Nombre = {self.getNombre()}, Direccion = {self.getDireccion()}, Ciudad = {self.getCiudad()}, FechaInauguracion = {self.getFechaInauguracion()}"

    def __str__(self):
        return self.toString()
