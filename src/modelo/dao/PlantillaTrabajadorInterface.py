# -*- coding: utf-8 -*-
"""
Created on Thu May  9 13:48:35 2024

@author: ricar
"""

from typing import List
from abc import ABC, abstractmethod
from src.modelo.vo.PlantillaTrabajadorVO import PlantillaTrabajadorVO

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class TrabajadorInterface(ABC):
    @abstractmethod
    def getTrabajadores(self) -> List[PlantillaTrabajadorVO]:
        raise NotImplementedError("Método getUsuarios no implementado")
    
    @abstractmethod
    def insertTrabajador(self, almacen: PlantillaTrabajadorVO):
        raise NotImplementedError("Método insertUsuario no implementado")