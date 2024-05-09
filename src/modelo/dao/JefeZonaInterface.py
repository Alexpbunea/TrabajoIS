# -*- coding: utf-8 -*-
"""
Created on Thu May  9 13:40:44 2024

@author: ricar
"""

from typing import List
from abc import ABC, abstractmethod
from src.modelo.vo.JefeZonaVO import JefeZona

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class JefeZonaInterface(ABC):
    @abstractmethod
    def getJefesZona(self) -> List[JefeZona]:
        raise NotImplementedError("Método getUsuarios no implementado")
    
    @abstractmethod
    def insertJefeZona(self, almacen: JefeZona):
        raise NotImplementedError("Método insertUsuario no implementado")