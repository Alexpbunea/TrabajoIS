# -*- coding: utf-8 -*-
"""
Created on Thu May  9 13:07:46 2024

@author: ricar
"""

from typing import List
from abc import ABC, abstractmethod
from src.modelo.vo.AlmacenVO import AlmacenVO

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class AlmacenInterface(ABC):
    @abstractmethod
    def getAlmacenes(self) -> List[AlmacenVO]:
        raise NotImplementedError("Método getUsuarios no implementado")
    
    @abstractmethod
    def insertAlmacen(self, almacen: AlmacenVO):
        raise NotImplementedError("Método insertUsuario no implementado")